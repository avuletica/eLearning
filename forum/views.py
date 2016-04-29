from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.text import slugify
from django.utils import timezone

from .forms import *
from .models import *


@login_required()
def forum(request):
    topic_list = Topic.objects.all().order_by('-stamp_updated')
    add_new_topic = AddNewTopic(request.POST or None)

    path = request.path.split('/')[1]
    redirect_path = path
    path = path.title()

    search = request.GET.get("search")
    if search:
        topic_list = topic_list.filter(subject__startswith=search)

    paginator = Paginator(topic_list, 10)

    if add_new_topic.is_valid():
        instance = add_new_topic.save(commit=False)
        instance.author = request.user
        slug = slugify(instance.subject)
        exists = Topic.objects.filter(slug=slug).exists()
        max_id = Topic.objects.latest('id').id
        max_id += 1
        # If slug exist append slug by id
        if exists:
            slug = "%s-%s" % (slug, max_id)

        instance.slug = slug
        instance.save()
        return redirect(reverse("forum"))

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "title": "Forum",
        "add_new_topic_form": add_new_topic,
        "topic_list": queryset,
        "path": path,
        "redirect_path": redirect_path,
    }

    return render(request, "forum/forum.html", context)


@login_required()
def topic(request, slug=None):
    add_new_comment = AddNewComment(request.POST or None)
    topic_id = Topic.objects.get(slug=slug)
    comment_list = Comment.objects.filter(comment_fk=topic_id)

    path = request.path.split('/')[1]
    redirect_path = path
    path = path.title()

    context = {
        "title": Topic.objects.get(slug=slug).subject,
        "add_new_comment_form": add_new_comment,
        "path": path,
        "comment_list": comment_list,
        "first_comment": Topic.objects.get(slug=slug).topic_message,
        "first_comment_timestamp": Topic.objects.get(slug=slug).stamp_created,
        "first_comment_author": Topic.objects.get(slug=slug).author,
        "redirect_path": redirect_path,
    }

    if add_new_comment.is_valid():
        instance = add_new_comment.save(commit=False)
        instance.author = request.user
        instance.comment_fk = Topic.objects.get(slug=slug)
        topic_object = Topic.objects.get(slug=slug)
        topic_object.comment_count += 1
        topic_object.stamp_updated = timezone.now()
        topic_object.save()
        instance.save()
        return redirect(reverse(topic, kwargs={'slug': slug,}))

    return render(request, "forum/topic.html", context)

/**
 * Created by ante on 4/28/16.
 */
$(document).ready(function () {
    // Bind the event handler to the "submit" JavaScript event
    $('.add-topic form').submit(function () {
        var $subject = $.trim($('#id_subject').val());
        var formData = tinyMCE.activeEditor.getContent({format: 'raw'});

        // Strip html tags from formData
        var regex = /(<([^>]+)>)/ig;
        var editorContent = formData.replace(regex, "");


        // Check if empty of not
        if ($subject === '' || editorContent === '') {
            alert("Can't submit empty fields");
            return false;
        }
    });

    var $topic = $(".add-btn");
    var $returnLink = $(".return-link");
    var $block = $(".add-topic");
    $topic.on("click", handleAddTopicClick);
    $returnLink.on("click", handleAddTopicClick);

    function handleAddTopicClick() {
        $block.toggle();
        $topic.toggle();
        $returnLink.toggle();

        $('html,body').animate({
            scrollTop: $(window).scrollTop() + block.height() / 2
        })
    }

});

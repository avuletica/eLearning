/**
 * Created by ante on 4/28/16.
 */
$(document).ready(function () {
    var topic = $(".add-btn");
    var returnLink = $(".return-link");
    var block = $(".add-topic");
    topic.on("click", handleAddTopicClick);
    returnLink.on("click", handleAddTopicClick);

    function handleAddTopicClick() {
        block.toggle();
        topic.toggle();
        returnLink.toggle();

        $('html,body').animate({
            scrollTop: $(window).scrollTop() + block.height()/2
        })
    }

    // Bind the event handler to the "submit" JavaScript event
    $('.add-topic form').submit(function () {
        var check = $.trim($('#id_topic_message').val());
        var check2 = $.trim($('#id_subject').val());

        // Check if empty of not
        if (check === '' || check2 === '') {
            alert("Can't submit empty fields");
            return false;
        }
    });
});

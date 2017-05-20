$(document).ready(function(){

    $(".arrow").click(function(e){
		var postBox = $(this).parent().siblings(".post-box");
        var postTitle = $(this).parent();
        if(postBox.is( ":hidden" )){
            postTitle.children().css("opacity","1");
            postBox.slideToggle();
            $(this).text(String.fromCharCode(9783));
        }
        else if(postBox.is( ":visible" )){
            postBox.slideToggle();
            $(this).text(String.fromCharCode(9776));
            postTitle.children().css("opacity","0.4");
        }
    });
});

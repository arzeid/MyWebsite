

$(document).ready(function(){

    $(".arrow").click(function(e){
		var postBox = $(this).siblings(".post-box");
        var postTitle = $(this).siblings(".post-title");
        if(postBox.is( ":hidden" )){
            postTitle.css("opacity","1");
            $(this).css("opacity","1");
            postBox.slideToggle();
            $(this).text(String.fromCharCode(9783));
        }
        else if(postBox.is( ":visible" )){
            postBox.slideToggle();
            $(this).text(String.fromCharCode(9776));
            postTitle.css("opacity","0.4");
            $(this).css("opacity","0.4");
        }
    });
});
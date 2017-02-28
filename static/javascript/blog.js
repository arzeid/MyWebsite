

$(document).ready(function(){

    $(".arrow").click(function(e){
		var postBox = $(this).siblings(".post-box");
        if(postBox.is( ":hidden" )){
            postBox.slideToggle();
            $(this).text(String.fromCharCode(9652));
        }
        else if(postBox.is( ":visible" )){
            postBox.slideToggle();
            $(this).text(String.fromCharCode(9662));
        }
    });
});
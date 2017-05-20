$(document).ready(function(){
    $(".dropdown").click(function(e){
        e.stopPropagation();
        $(this).siblings(".dropdown").find(".dropdown-content").hide();
        $(this).find(".dropdown-content").toggle();
    });
    $("#topnav-menu-button").click(function(e){
        $(this).parent().siblings(".topnav").slideToggle();
    });

    $(window).resize(function() {
        if($("#topnav-menu-button").is( ":hidden" )){
            $(".topnav").show();
        }
        else if($("#topnav-menu-button").is( ":visible" )){
            $(".topnav").hide();
        }
    });
});


$(document).click(function(){
    $(".dropdown-content").hide();
});

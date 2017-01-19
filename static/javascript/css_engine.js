/*
$(function(){
    $('body').css('overflow-y', 'auto');
    var b = $('body');
    var normalWidth = 0;
    var scrollWidth = 0;
    if(b.prop('scrollHeight')>b.height()){
        normalWidth = window.innerWidth;
        scrollWidth = normalWidth - b.width();
        $('#container').css({marginRight:'-'+scrollWidth+'px'});
        $('#container').css({paddingRight:'-'+scrollWidth+'px'});
    }
});
*/

$(document).ready(function(){
    $(".dropdown").click(function(e){
        e.stopPropagation();
        $(this).siblings(".dropdown").find(".dropdown-content").hide();
        $(this).find(".dropdown-content").toggle();
    });
    $("#topnav-menu").click(function(e){
        $(this).siblings(".topnav").slideToggle();
    });
    $(window).resize(function() {
        if($(window).width() > 500) {
            $(".topnav").show();
        }
    });
});


$(document).click(function(){
    //$(".dropdown-content").hide('slow'); 
    $(".dropdown-content").hide(); 
});

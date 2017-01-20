/*
$(function(){
    $('body').css('overflow-y', 'auto');
    var b = $('body');
    var normalWidth = 0;
    var scrollWidth = 0;
    if(b.prop('scrollHeight')>b.height()){
        normalWidth = window.innerWidth;
        scrollWidth = normalWidth - b.width();
        $('body').css({marginRight:'-'+scrollWidth+'px'});
    }
});
*/

/*
function scrollbarWidth() { 
    var div = $('<div style="width:50px;height:50px;overflow:hidden;position:absolute;top:-200px;left:-200px;"><div style="height:100px;"></div>'); 
    // Append our div, do our calculation and then remove it 
    $('body').append(div); 
    var w1 = $('div', div).innerWidth(); 
    div.css('overflow-y', 'scroll'); 
    var w2 = $('div', div).innerWidth(); 
    $(div).remove(); 
    return (w1 - w2); 
}
*/

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
    //$(".dropdown-content").hide('slow'); 
    $(".dropdown-content").hide(); 
});

/*
function get_url_count() {
    $.getJSON($SCRIPT_ROOT + '/shorten_url_count', {
        }, function(data) {
            $("#url_count").text(data.url_count);
        });
        return false;
}

setInterval(function(){
    get_url_count()
}, 10000);
*/

function ValidURL(str) {
  var pattern = new RegExp('^(https?:\/\/)?'+ // protocol
    '((([a-z\d]([a-z\d-]*[a-z\d])*)\.)+[a-z]{2,}|'+ // domain name
    '((\d{1,3}\.){3}\d{1,3}))'+ // OR ip (v4) address
    '(\:\d+)?(\/[-a-z\d%_.~+]*)*'+ // port and path
    '(\?[;&a-z\d%_.~+=-]*)?'+ // query string
    '(\#[-a-z\d_]*)?$','i'); // fragment locater
  if(!pattern.test(str)) {
    return false;
  } else {
    return true;
  }
}


function isValidUrl(url){
    var myVariable = url;
    var pattern = /^(http|https|ftp):\/\/[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$/i;
    if(pattern.test(myVariable)) {
        return true;
    } else {
        return false;
    }   
}


$(document).ready(function(){

    $(".urlinput-button").click(function(){
        var url = $('.urlinput').val();
        
        if (isValidUrl(url)==true){
            //$('.urlinput-button').val("Shorten "+String.fromCharCode(10004));
            $('.urlinput-button').prop('disabled', false);
            $('.urlinput-button').val("Shorten");
        }
        else{
            $('.urlinput-button').val("Invalid URL");
            $('.urlinput-button').prop('disabled', true);
            //$('.urlinput').addClass('red');
        }
    });
    
    $(".urlinput").on('input keyup focus keypress change', function() {
        var url = $(this).val();
        if(url.length > 0)
        {
            if (isValidUrl(url)==true){
                //$('.urlinput-button').val("Shorten "+String.fromCharCode(10004));
                $('.urlinput-button').prop('disabled', false);
                $('.urlinput-button').val("Shorten");
            }
            else{
                $('.urlinput-button').val("Invalid URL");
                $('.urlinput-button').prop('disabled', true);
                //$('.urlinput').addClass('red');
            }
        }
    });
    
    $("form").submit(function(e){
        e.preventDefault();
        var url = $("form .urlinput").val();
        console.log(url);
        $.post($SCRIPT_ROOT + '/shorten/',
        {
          url: url,
        },
        function(data,status){
            //alert("Short URL: " + data.short_url+ 
            //      "\nClick Count: "+data.click_count);
            $('.urlinput-button').val('short link generated');
            $('#short_link').text('azeid.com'+data.short_url);
            $("#short_link").attr("href", $SCRIPT_ROOT+data.short_url);
        }, 'json');
    });
});




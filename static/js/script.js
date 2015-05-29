function getCookie(name) {
  var matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

function randWDn(n){
  var s ='';
  while(s.length < n)
    s += Math.random().toString(36).slice(2, 12);
  return s.substr(0, n);
}

$(document).ready(function(){

    $(document).on('click', '.login_show', function(){
        $("#popup_box").remove();
        $("body").append('<div id="popup_box" style="display:none"></div>');
        $("#popup_box").load("/login/", function(){
            $(document).on('click', '.login', function(){
                alert("ok");
                $.get("/login/",
                    {
                        'email': $("#email").val(),
                        'password': $("#password").val()
                    },
                    function(data){
                        alert(data);
                        if(data === 'true'){
                            $("#popup_box").fadeOut(300);
                            location.reload()
                        }
                        else {
                            $("#popup_box").html(data);
                        }
                    }
                );
            });
        });
        $("#popup_box").fadeIn(300);
        return false;
    });

    $(document).on('click', '.registration_show', function(){
        $("#popup_box").remove();
        $("body").append('<div id="popup_box" style="display:none"></div>');
        //$("#popup_box").css({"margin-top": "-160px"});
        $("#popup_box").load("/registration/");
        $("#popup_box").fadeIn(400);
        return false;
    });

    $(document).on('click', '#registration_button', function() {
        $.get("/registration/",
            {
                "csrftoken": getCookie("csrftoken"),
                "first_name": $("#first_name").val(),
                "email": $("#email").val(),
                "password": $("#password").val(),
                "password_again": $("#password_again").val()
            },
            function(data){
                alert(data);
                $("#popup_box").html(data);
            }
        );
    });


    $("#input-price").ionRangeSlider({
        type: "double",
        min: 0,
        max: 1500,
        from: 100,
        to: 1000
    });
    $("#input-size").ionRangeSlider({
        type: "double",
        min: 0,
        max: 1500,
        from: 100,
        to: 1000
    });
    $(".carousel").sliderkit({
        auto:false,
        shownavitems:4,
        circular:true
    });
    $('select').styler();


    $(".small-cart-img img").each(function(index, element){
        if ($(element).width() > $(element).height())
        {
            $(element).css({'width': 'auto', 'height': '100%'});
        }
    });



    /* ================  Корзина  ================ */

    $(document).on('click', '.add_product', function() {
        $.post("/cart/add_product/",
            {
                csrfmiddlewaretoken: getCookie("csrftoken"),
                product_id: $(this).attr("data-id"),
                size: $('input[name=size]:checked').val(),
                count: $("#id_count").val(),
                color: $(".jq-selectbox__select-text").html()
            },
             function(msg){
                 alert(msg);
                 $('input[name=size]:checked').removeAttr("checked");
                 $("#id_count").val(1);
            }
        );
        return false;
    });


    $(document).on('click', '.change_count', function() {
        $.post("/cart/change_count_product/",
            {
                csrfmiddlewaretoken: getCookie("csrftoken"),
                product_id: $(this).attr("data-id"),
                count: $(this).attr("data-count")
            },
            function(data) {
                $(".user_cart").html(data);
            }
        );
    });


});
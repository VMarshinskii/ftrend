/**
 * Created by VladCH on 08.05.2015.
 */

$(document).ready(function () {
    $("#input-price").ionRangeSlider({
        type: "double",
        min: 0,
        max: $("#input-price").attr('data-max'),
        from: 0,
        to: $("#input-price").attr('data-max')
    });
    $("#input-size").ionRangeSlider({
        type: "double",
        min: 0,
        max: 160,
        from: 0,
        to: 160
    });
    $(".carousel").sliderkit({
        auto:false,
        shownavitems:4,
        circular:true
    });
    $('select').styler();
});
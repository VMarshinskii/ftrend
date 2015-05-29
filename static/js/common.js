/**
 * Created by VladCH on 08.05.2015.
 */

$(document).ready(function () {
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
});
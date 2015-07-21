/**
 * Created by VladCH on 08.05.2015.
 */

$(document).ready(function () {
    $("#input-price").ionRangeSlider({
        type: "double",
        min: 0,
        max: 10000,
        from: 0,
        to: 10000
    });
    $("#input-size").ionRangeSlider({
        type: "double",
        min: 0,
        max: 182,
        from: 0,
        to: 182
    });
    $(".carousel").sliderkit({
        auto:false,
        shownavitems:4,
        circular:true
    });
    $('select').styler();
});
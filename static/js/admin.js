function getCookie(name) {
  var matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

$(document).ready(function(){

    if($("input").is("#id_sizes"))
    {
        $('#id_sizes').selectize({
            delimiter: ',',
            create: function(input) {
                return {
                    value: input,
                    text: input
                }
            }
        });
    }

    if($("select").is("#id_colors"))
    {
        $('#id_colors').selectize({
            delimiter: ','
        });
    }

    if($("select").is("#id_similar"))
    {
        $('#id_similar').selectize({
            delimiter: ','
        });
    }

    if($("select").is("#id_products"))
    {
        $('#id_products').selectize({
            delimiter: ','
        });
    }

    if($("select").is("#id_age"))
    {
        $('#id_age').selectize({
            delimiter: ','
        });
    }

    if($("select").is("#id_collection"))
    {
        $('#id_collection').selectize({
            delimiter: ','
        });
    }


    if($("input").is("#id_images"))
    {
        $("#id_images").hide();

        if($("div").is(".field-image"))
        {
            $(".field-image").hide();
        }

        var html = '<div class="adminBoxImg adminBoxImgLast"></div>';
        $("#id_images").after(html);

        var images = $("#id_images").val().split(";");
        for (var i = 0; i < images.length; i++)
        {
            var image = $("#id_image").val();
            var id_active = "";
            if (image == images[i])
            {
                id_active = "hidden_image_active";
            }

            if (images[i] != "")
            {
                var html = '<div class="adminBoxImg">\
                                <img src="/static/uploads/' + images[i] + '" alt="">\
                                <div class="adminBoxSettingsImages">\
                                    <img class="adminBoxImgClose" src="/static/images/close_icon.png" data-image="' + images[i] + '" alt="Удалить">\
                                    <img class="adminBoxImgHead" src="/static/images/icon_writing.png" data-image="' + images[i] + '" id=' + id_active + ' alt="Главная">\
                                </div>\
                            </div>\
                            ';
                $(".adminBoxImgLast").before(html);
            }

        }
    }





    if($(".file-upload").is())
    {
        var path = $(".file-upload").children("a").attr("href");
        $(".file-upload").children("a").attr("href", '/' + path);
        $(".file-upload").children("a").html('<img width="260px" class="adminImageField" src="/' + path + '"/>');
        var content = $(".file-upload").html().replace("На данный момент: ", '');
        $(".file-upload").html(content);
    }


    var myDropzone = new Dropzone(".adminBoxImgLast",
        {
            url: "/admin/upload_image/",
            sending: function(file, xhr, formData) {
                formData.append("csrfmiddlewaretoken", getCookie("csrftoken"));
            },
            success: function(file, response)
            {
                var html = '<div class="adminBoxImg">\
                                <img src="/static/uploads/' + response + '" alt="">\
                                <div class="adminBoxSettingsImages">\
                                    <img class="adminBoxImgClose" src="/static/images/close_icon.png" data-image="' + response + '" alt="Удалить">\
                                    <img class="adminBoxImgHead" src="/static/images/icon_writing.png" data-image="' + response + '" alt="Главная">\
                                </div>\
                            </div>\
                            ';
                $(".adminBoxImgLast").before(html);

                var images = $("#id_images").val();
                $("#id_images").val(images + ";" + response);

                var image = $("#id_image").val();
                if (image == "")
                {
                    $("#id_image").val(response);
                    $(".adminBoxImgHead").first().attr('id', 'hidden_image_active');
                }
            }
        }
    );

    $(document).on('click', '.adminBoxImgHead', function(){
        $("#hidden_image_active").attr('id', '');
        $(this).attr('id', 'hidden_image_active');
        var image = $(this).attr("data-image");
        $("#id_image").val(image);
    });

    $(document).on('click', '.adminBoxImgClose', function(){
        var image = $(this).attr("data-image");
        var images = $("#id_images").val().replace(";" + image, "");
        $("#id_images").val(images);
        $(this).parents(".adminBoxImg").remove();

        var image_one = $("#id_image").val();

        if (image == image_one)
        {
            var img = $(".adminBoxImgHead").first().attr('data-image');
            $("#id_image").val(img);
            $(".adminBoxImgHead").first().attr('id', 'hidden_image_active');
        }

    });


    if($("div").is(".field-colors")) {
        alert("ok");
        $(".field-colors").find(".controls").html('');

        $(document).on('click', ".field-sizes .item", function () {

            $(".field-colors").find(".controls").html('<div class="related-widget-wrapper" id="ajax_size_colors"></div>');
            $("#ajax_size_colors").load("/admin/size_colors/sada/");

            $("#ajax_size_colors").selectize({
                delimiter: ','
            });

            var id_size_colors = $("#id_size_colors").val();
            var item_active = $(this).attr('data-value');
            $("#id_size_colors").val(id_size_colors + ";" + item_active);
        });

    }


});
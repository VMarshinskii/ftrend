from django.shortcuts import render_to_response, HttpResponse
from ftrend.additions import upload_file
from catalog.models import Color


def video_upload(request):
    if request.method == 'POST' and request.user.is_authenticated():
        f = request.FILES['file']
        path = "/static/uploads/"
        url = upload_file(f, path)
        return HttpResponse(url)
    return HttpResponse("no")


def size_colors(request, data):
    if request.user.is_authenticated():
        selected_colors = data.split(",")
        colors = []
        for color in Color.objects.all():
            if color.id in selected_colors:
                color.selected = 'selected="selected"'
            colors.append(color)
        return render_to_response("size_colors.html", {'colors': colors})
    return HttpResponse("False")
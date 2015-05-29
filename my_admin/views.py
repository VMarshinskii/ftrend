from django.shortcuts import render_to_response, HttpResponse
from ftrend.additions import upload_file


def video_upload(request):
    if request.method == 'POST':
        f = request.FILES['file']
        path = "\static\uploads\\"
        url = upload_file(f, path)
        return HttpResponse(url)
    return HttpResponse("no")
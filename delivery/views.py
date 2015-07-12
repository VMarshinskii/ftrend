from django.shortcuts import render_to_response
from models import DeliveryCDEK

def points_sdk_view(request):
    return render_to_response("points_sdk_view.html")


def point_sdk_view(request, url):
    points = DeliveryCDEK.objects.filter(url=url)
    return render_to_response("point_sdk_view.html", {
        'city': points[0].name,
        'points': points
    })

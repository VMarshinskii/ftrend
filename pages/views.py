from django.shortcuts import render_to_response, Http404
from models import Page


def page_view(request, url="None"):
    try:
        page = Page.objects.get(url=url)
    except Page.DoesNotExist:
        raise Http404
    return render_to_response("page.html", {'page': page})

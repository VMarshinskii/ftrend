from django.shortcuts import render_to_response


def create_order(request):
    return render_to_response("create_order.html", {'user': request.user})

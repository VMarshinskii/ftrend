from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from forms import OrderForm


def create_order(request):
    # args = {}
    # args.update(csrf(request))
    #
    # if request.POST:
    #     form = OrderForm(request.POST)
    #     if form.is_valid():


    return render_to_response("create_order.html", {'user': request.user})

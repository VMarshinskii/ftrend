from django.shortcuts import render_to_response, Http404
from sale.models import Sale


def index_view(request):
    sales = list(Sale.objects.filter(is_active=True))
    sale_1 = sales.pop(0)
    return render_to_response("index.html", {
        'user': request.user,
        'sale_1': sale_1,
        'sales': sales
    })


def sale_view(request, url=''):
    try:
        sale = Sale.objects.get(url=url)
        products = sale.products.all()
        return render_to_response("sale.html", {
            'user': request.user,
            'products': products,
            'sale': sale,
        })
    except Sale.DoesNotExist:
        raise Http404

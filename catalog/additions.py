# -*- coding: utf-8 -*-

def products_filter(args):
    products_new = []
    print args
    start_price = args['start_price']
    stop_price = args['stop_price']
    collections = args['collections']

    for product in args['products']:
        if start_price <= product.price <= stop_price:
            for pr_coll in product.collection.all():
                if pr_coll.id in collections:
                    products_new.append(product)

    return products_new

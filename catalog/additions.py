# -*- coding: utf-8 -*-

def products_filter(args):
    products_new = []
    start_price = args['start_price']
    stop_price = args['stop_price']
    collections = args['collections']

    for product in args['products']:
        if start_price <= product.price <= stop_price:
            print product.name
            for pr_coll in product.collection.all().values_list('id'):
                print pr_coll
                if pr_coll in collections:
                    products_new.append(product)

    return products_new

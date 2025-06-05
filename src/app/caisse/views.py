from django.shortcuts import render, HttpResponse
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from .models import Product, Stock, Sale, LineSale, Store, Product_Depot, engine


Session = sessionmaker(bind=engine)
session = Session()

def home(request):
    return render(request, "home.html")

# def sales_report(request):
#     sales1 = get_sales_by_store(1)
#     sales2 = get_sales_by_store(2)
#     sales3 = get_sales_by_store(3)
#     sales4 = get_sales_by_store(4)
#     sales5 = get_sales_by_store(5)

#     return render(request, "report.html", {
#         "sales1": sales1,
#         "sales2": sales2,
#         "sales3": sales3,
#         "sales4": sales4,
#         "sales5": sales5
#     })

def search_products(request):

    r_id = request.GET.get('id')
    
    if not r_id: 
        products = Product.get_all_products()
        list_stocks_store_1 = Store.get_stock_by_store(session, 1)
        list_stocks_store_2 = Store.get_stock_by_store(session, 2)
        list_stocks_store_3 = Store.get_stock_by_store(session, 3)
        list_stocks_store_4 = Store.get_stock_by_store(session, 4)
        list_stocks_store_5 = Store.get_stock_by_store(session, 5)

        zipped1 = zip(products, list_stocks_store_1)
        zipped2 = zip(products, list_stocks_store_2)
        zipped3 = zip(products, list_stocks_store_3)
        zipped4 = zip(products, list_stocks_store_4)
        zipped5 = zip(products, list_stocks_store_5)

        return render(request, "products.html", 
            {"zipped1": zipped1,
            "zipped2": zipped2,
            "zipped3": zipped3,
            "zipped4": zipped4,
            "zipped5": zipped5}
        )
    else:
        products = []
        product = get_product_by_id(r_id)

        if not product: 
            return HttpResponse("Product not found")
        
        products.append(product)
        stock1 = get_stock(product.id, 1)
        stock2 = get_stock(product.id, 2)
        stock3 = get_stock(product.id, 3)
        stock4 = get_stock(product.id, 4)
        stock5 = get_stock(product.id, 5)
        stocks = [stock1, stock2, stock3, stock4, stock5]
        

        zipped1 = zip(products, stocks)

        return render(request, "products.html", 
            {"zipped1": zipped1}
        )

def dashboard_logistique(request):
    depots = Product_Depot.get_all_product_depots(session=session)
    return render(request, "stock-central.html", {"depots": depots})





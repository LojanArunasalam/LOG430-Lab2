from django.shortcuts import render, HttpResponse
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from .models import User, Product, Sale, LineSale, Stock, Store, Product_Depot, engine

Session = sessionmaker(bind=engine)
session = Session()

def home(request):
    return render(request, "home.html")

def sales_report(request):
    sales1 = get_sales_by_store(1)
    sales2 = get_sales_by_store(2)
    sales3 = get_sales_by_store(3)
    sales4 = get_sales_by_store(4)
    sales5 = get_sales_by_store(5)

    return render(request, "report.html", {
        "sales1": sales1,
        "sales2": sales2,
        "sales3": sales3,
        "sales4": sales4,
        "sales5": sales5
    })

def search_products(request):
    products = get_all_products()
    list_stocks_store_1 = get_stock_by_store(1)
    list_stocks_store_2 = get_stock_by_store(2)
    list_stocks_store_3 = get_stock_by_store(3)
    list_stocks_store_4 = get_stock_by_store(4)
    list_stocks_store_5 = get_stock_by_store(5)

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

def dashboard_logistique(request):
    depot = session.query(Product_Depot).all()
     

    return render(request, "dashboard.html", {"depot" : depot})

# Product Controller
def get_product_by_id(id):
    product = session.query(Product).filter_by(id=id).first()
    if not product:
        return None
    return product

def get_product_by_category(category):
    products = session.query(Product).filter_by(category=category).all()
    if not products:
        return None
    return products

def get_all_products():
    products = session.query(Product).all()
    if not products:
        return None
    return products


# Sale Controller
def get_sales_by_store(store_id):
    sales = session.query(Sale).filter_by(store=store_id).all()
    if not sales:
        return None
    return sales

def get_sales_by_user(user_id):
    sales = session.query(Sale).filter_by(user=user_id)
    if not sales:
        return None
    return 

def get_all_sales():
    sales = session.query(Sale).all()
    return sales


# Stock Controller
def get_stock(id, storeid):
    stock_product = session.query(Stock).filter_by(id=id, store=storeid).first()
    return stock_product

def get_stock_by_store(storeid):
    list_stocks = session.query(Stock).filter_by(store=storeid).all()
    return list_stocks 

# Line Sale Controller 
def get_line_sales_by_sale(sale_id):
    list_line_sales = session.query(LineSale).filter_by(sale=sale_id)
    return list_line_sales

# Store Controller
def get_all_stores():
    stores = session.query(Store).all()
    if not stores:
        return None
    return stores

def get_stores_by_name(name):
    stores = session.query(Store).filter_by(name=name)
    if not stores:
        return None
    return stores

# def create_line_sale(product, quantite_voulu):
#     line_sale = LineSale(quantite=quantite_voulu, prix=quantite_voulu*product.prix_unitaire)
#     product.ligne_vente.append(line_sale)
#     return line_sale

# def create_sale(lines_sales):
#     total = 0
#     for line in lines_sales:
#         total = total + line.prix
#         session.add(line)

#     sale = Sale(total=total)
#     sale.line_vente.extend(lines_sales)

#     return sale
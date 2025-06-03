from django.shortcuts import render, HttpResponse
from sqlalchemy.orm import sessionmaker
from .models import User, Product, Sale, LineSale, Stock, engine

Session = sessionmaker(bind=engine)
session = Session()

# Create your views here.
def home(request):
    return render(request, "home.html")

def get_product_by_store(request):
    products_store = session.query(Product).filter_by(store=1)

    if not products_store:
        return None

    return render(request, "products.html", {"products1": products_store})

def get_stock(id):
    stock_product = session.query(Product).filter_by(id=id).first()
    stock = session.query(Stock).filter_by(product=stock_product.id).all()
    return stock

def create_line_sale(product, quantite_voulu):
    line_sale = LineSale(quantite=quantite_voulu, prix=quantite_voulu*product.prix_unitaire)
    product.ligne_vente.append(line_sale)
    return line_sale

def create_sale(lines_sales):
    total = 0
    for line in lines_sales:
        total = total + line.prix
        session.add(line)

    sale = Sale(total=total)
    sale.line_vente.extend(lines_sales)

    return sale
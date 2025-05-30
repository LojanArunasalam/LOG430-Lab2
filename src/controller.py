from sqlalchemy.orm import sessionmaker

from models import User, Product, Sale, LineSale, engine

# Session that will do operations to the database
Session = sessionmaker(bind=engine)
session = Session()

def get_product_by_id(id):
    return session.query(Product).filter_by(id=id).first()

def get_stock(id):
    stock_product = session.query(Product).filter_by(id=id).first()
    return stock_product.stock

def update_stock(product, quantite):
    product.stock = product.stock - quantite
    

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


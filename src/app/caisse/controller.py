from models import Product, Depot, Stock, Sale, LineSale, Store, User, Product_Depot, engine 
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

def restock_from_depot(product_id, quantity, store_id):
    stock = Stock.get_stock_by_product_and_store(session, product_id, store_id)
    product_depot = Product_Depot.get_product_depot_by_product_id(session, product_id)
    if not stock:
        return Exception("Product not found in store stock")
    if not product_depot:
        return Exception("Product not found in depot stock")
    
    stock.quantite += quantity
    product_depot.quantite_depot -= quantity
    if product_depot.quantite_depot < 0:
        return Exception("Not enough stock in depot to restock the store")
    session.commit()
    return {"stocks": stock, "product_depot": product_depot}

def create_line_sale(product, quantite_voulu):
    line_sale = LineSale(quantite=quantite_voulu, prix=quantite_voulu*product.prix_unitaire)
    product.ligne_vente.append(line_sale)

    session.add(line_sale)
    session.commit()
    return line_sale

def create_sale(lines_sales):
    total = 0
    for line in lines_sales:
        total = total + line.prix
        session.add(line)

    sale = Sale(total=total)
    sale.line_vente.extend(lines_sales)

    session.add(sale)
    session.commit()

    return sale
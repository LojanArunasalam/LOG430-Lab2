from .models import Product, Stock, Sale, LineSale, Store, User, Product_Depot, engine 
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
    if product_depot.quantite_depot - quantity < 0:
        return Exception("Not enough stock in depot to restock the store")
    product_depot.quantite_depot -= quantity
    session.commit()

def get_product_with_stocks(store_id):
    products = Product.get_all_products(session)
    stocks = []
    for product in products: 
        stock = Stock.get_stock_by_product_and_store(session, product.id, store_id)
        if stock:
            stocks.append(stock)
    return zip(products, stocks)

def performances():
    # Generate the total in sales for each stores, and for each stock of the products in each store, indicates whether the stock is sufficient or not.
    stores = Store.get_all_stores(session)
    totals = []
    stocks = []
    store_ids = []
    for store in stores:
        sales = Sale.get_sales_by_store(session, store.id)
        total_store = sum(sale.total for sale in sales)
        totals.append(total_store)
        stocks_store = Stock.get_stock_by_store(session, store.id)
        stocks.append(stocks_store)
        store_ids.append(store.id)


    performances_data = zip(totals, stocks, store_ids)
    return performances_data

def generate_report(store_id):
    report = {}
    sales = Sale.get_sales_by_store(session, store_id)
    most_sold_product = None
    max_quantity = 0
        
    for sale in sales:
        line_sales = LineSale.get_line_sales_by_sale(session, sale.id)
        for line_sale in line_sales:
            if line_sale.quantite > max_quantity:
                max_quantity = line_sale.quantite
                most_sold_product = Product.get_by_id(session, line_sale.product)

    report["store_id"] = store_id
    report["sales"] = sales
    report["most_sold_product"] = most_sold_product
    report["max_quantity"] = max_quantity


    return report
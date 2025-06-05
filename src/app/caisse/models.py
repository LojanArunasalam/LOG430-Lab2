from django.db import models
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine 

db_url = 'postgresql+psycopg2://admin:admin@10.194.32.165:5432/postgres'
engine = create_engine(db_url)
Base = declarative_base()

class LineSale(Base):
    __tablename__ = "line_sales" 

    id = Column(Integer, primary_key=True)
    quantite = Column(Integer)
    prix = Column(Float)

    #Relationships
    sale = Column(Integer, ForeignKey("sales.id"))
    product = Column(Integer, ForeignKey("products.id"))

    @classmethod
    def get_by_id(cls, session, id):
        line_sale = session.query(cls).filter_by(id=id).first()
        if not line_sale:
            return None
        return line_sale
    
    @classmethod
    def get_line_sales_by_sale(cls, session, sale_id):
        line_sales = session.query(cls).filter_by(sale=sale_id).all()
        if not line_sales:
            return None
        return line_sales
    

class Stock(Base):
    __tablename__ = "stocks"
    id = Column(Integer, primary_key=True)
    quantite = Column(Integer, primary_key=True)

    #Relationsips
    product = Column(Integer, ForeignKey("products.id"))
    store = Column(Integer, ForeignKey("stores.id"))

    def __str__(self):
        return f"{self.quantite}"

    @classmethod
    def get_stock_by_id(cls, session, id):
        stock = session.query(cls).filter_by(id=id).first()
        if not stock:
            return None
        return stock
    
    @classmethod
    def get_stock_by_store(cls, session, store_id):
        stocks = session.query(cls).filter_by(store=store_id).all()
        if not stocks:
            return None
        return stocks
    
    @classmethod
    def get_stock_by_product_and_store(cls, session, product_id, store_id):
        stock = session.query(cls).filter_by(product=product_id, store=store_id).first()
        if not stock:
            return None
        return stock
        

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    description = Column(String)
    prix_unitaire = Column(Float)
    
    #Relationships
    line_sale = relationship(LineSale)
    stock = relationship(Stock)

    @classmethod
    def get_by_id(cls, session, id):
        product = session.query(cls).filter_by(id=id).first()
        if not product:
            return None
        return product
    
    @classmethod
    def get_all_products(cls, session):
        products = session.query(cls).all()
        if not products:
            return None
        return products
    
    @classmethod
    def get_product_by_category(cls, session, category):
        products = session.query(cls).filter_by(category=category).all()
        if not products:
            return None
        return products


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    total = Column(Float)

    #Relationships
    line_vente = relationship(LineSale)
    user = Column(ForeignKey("users.id"))
    store = Column(ForeignKey("stores.id"))

    @classmethod
    def get_sales_by_store(cls, session, store_id):
        sales = session.query(cls).filter_by(store=store_id).all()
        if not sales:
            return None
        return sales
    
    @classmethod
    def get_sales_by_user(cls, session, user_id):
        sales = session.query(cls).filter_by(user=user_id).all()
        if not sales:
            return None
        return sales
    
    @classmethod
    def get_all_sales(cls, session):
        sales = session.query(cls).all()
        if not sales:
            return None
        return sales

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    #Relationships
    sale = relationship(Sale)

    @classmethod
    def get_user_by_id(cls, session, id):
        user = session.query(cls).filter_by(id=id).first()
        if not user:
            return None
        return user
    
    @classmethod
    def get_all_users(cls, session):
        users = session.query(cls).all()
        if not users:
            return None
        return users
    

class Product_Depot(Base):
    __tablename__ = "products_depot"

    id = Column(Integer, primary_key=True)
    quantite_depot = Column(Integer)
    #Relationships
    product = Column(ForeignKey("products.id"))

    @classmethod
    def get_product_depot_by_product_id(cls, session, product_id):
        product_depot = session.query(cls).filter_by(id=product_id).first()
        if not product_depot:
            return None
        return product_depot
    
    @classmethod
    def get_all_product_depots(cls, session):
        product_depots = session.query(cls).all()
        if not product_depots:
            return None
        return product_depots


class Store(Base):
    # Includes the parent house (maison mere)
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    #Relationships
    stocks = relationship(Stock)
    sales = relationship(Sale)

    @classmethod
    def get_store_by_id(cls, session, id):
        store = session.query(cls).filter_by(id=id).first()
        if not store:
            return None
        return store
    
    @classmethod
    def get_all_stores(cls, session):
        stores = session.query(cls).all()
        if not stores:
            return None
        return stores
    
    @classmethod
    def get_stores_by_name(cls, session, name):
        store = session.query(cls).filter_by(name=name).first()
        if not store:
            return None
        return store
    
    
# Will create the database + the tables associated with it
Base.metadata.create_all(engine)
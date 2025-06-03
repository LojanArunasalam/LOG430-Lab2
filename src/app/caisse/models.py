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

class Stock(Base):
    __tablename__ = "stocks"
    id = Column(Integer, primary_key=True)
    quantite = Column(Integer, primary_key=True)

    #Relationsips
    product = Column(Integer, ForeignKey("products.id"))
    store = Column(Integer, ForeignKey("stores.id"))

    def __str__(self):
        return f"{self.quantite}"

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


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    total = Column(Float)

    #Relationships
    line_vente = relationship(LineSale)
    user = Column(ForeignKey("users.id"))
    store = Column(ForeignKey("stores.id"))

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    #Relationships
    sale = relationship(Sale)

class Product_Depot(Base):
    __tablename__ = "products_depot"

    id = Column(Integer, primary_key=True)
    quantite_depot = Column(Integer)
    #Relationships
    products = Column(ForeignKey("products.id"))
    


class Store(Base):
    # Includes the parent house (maison mere)
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    #Relationships
    stocks = relationship(Stock)
    sales = relationship(Sale)
    
# Will create the database + the tables associated with it
Base.metadata.create_all(engine)
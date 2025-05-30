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

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    description = Column(String)
    prix_unitaire = Column(Float)
    stock = Column(Integer)

    #Relationships
    ligne_vente = relationship(LineSale)


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    total = Column(Float)
    user = Column(ForeignKey("users.id"))

    #Relationships
    line_vente = relationship(LineSale)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    #Relationships
    sale = relationship(Sale)

# class CentralHub(Base):
#     __tablename__ = "central_hubs"

# class Store(Base):
#     __tablename_ = "stores"



# class SupplyRequest(Base):
#     __tablename__ = "supply_requests"


# Will create the database + the tables associated with it
Base.metadata.create_all(engine)
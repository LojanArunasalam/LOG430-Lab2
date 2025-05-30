import pytest
from src.models import User, Sale, LineSale, Product

def test_product():
    product = Product(
        name="Timbits",
        category="Snacks",
        description="Tiny donut balls",
        prix_unitaire=0.25,
        stock=100
    )
    assert product.name == "Timbits"
    assert product.stock == 100
    assert product.prix_unitaire == pytest.approx(0.25)

def test_sale():
    pass

def test_line_sale():
    pass

def test_user():
    pass
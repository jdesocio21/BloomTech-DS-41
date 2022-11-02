from acme import Product
from acme_report import generate_products


def test_default_product_price():
    '''Test default product price being 10.'''
    prod = Product('Test Product')
    assert prod.price == 10


def test_default_product_weight():
    '''Test default product weight being 20.'''
    prod = Product('Test Product')
    assert prod.weight == 20


def test_default_product_flammability():
    '''Test default product flammability being 0.5.'''
    prod = Product('Test Product')
    assert prod.flammability == 0.5


def test_default_product_explode():
    '''Test explode method.'''
    prod = Product('Test Product')
    assert prod.weight * prod.flammability == 10


def test_default_product_stealability():
    '''Test stealability method.'''
    prod = Product('Test Product')
    assert prod.price / prod.weight == 0.5


def test_generate_products_length():
    '''Test generate_products() returns a list of 30 products.'''
    prod_list = generate_products()
    assert len(prod_list) == 30

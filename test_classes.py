import pytest

from classes import Category
from classes import Products

@pytest.fixture
def check_correctness_of_category():
    return Category('Футболки', 'Футболки - удобный предмет одежды', ['женские футболки', 'мужские футболки', 'детские футболки'])


def test_init(check_correctness_of_category):
    assert check_correctness_of_category.name == 'Футболки'
    assert check_correctness_of_category.description == 'Футболки - удобный предмет одежды'
    assert check_correctness_of_category.goods == ['женские футболки', 'мужские футболки', 'детские футболки']


@pytest.fixture
def check_correctness_of_products():
    return Products("Футболки оверсайз", "Удобная футболка", 2000, 4)


def test_init_for_products(check_correctness_of_products):
    assert check_correctness_of_products.product_name == "Футболки оверсайз"
    assert check_correctness_of_products.product_description == "Удобная футболка"
    assert check_correctness_of_products.price == 2000
    assert check_correctness_of_products.quantity == 4


@pytest.fixture
def check_correct_init_number():
    return Category("Футболки", "Футболки - удобный предмет одежды", ['женские футболки', 'мужские футболки', 'детские футболки'])

def test_total_number(check_correct_init_number):
    assert check_correct_init_number.amount_of_unique_goods == 6
    assert check_correct_init_number.total_amount_of_categories == 2







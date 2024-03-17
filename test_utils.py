import pytest

from utils import Category
from utils import Products

@pytest.fixture
def check_correctness_of_category():
    return Category('Футболки', 'Футболки - удобный предмет одежды', ['женские футболки', 'мужские футболки', 'детские футболки'])


def test_init():
    assert check_correctness_of_category.name == 'Футболки'
    assert check_correctness_of_category.description == 'Футболки - удобный предмет одежды'
    assert check_correctness_of_category.goods == ['женские футболки', 'мужские футболки', 'детские футболки']


@pytest.fixture
def check_correctness_of_products():
    return Products("Футболки оверсайз", "Удобная футболка", 2000, 4)


def test_init_for_products():
    assert check_correctness_of_products.name == "Футболка оверсайз"
    assert check_correctness_of_products.description == "Удобная футболка"
    assert check_correctness_of_products.price == 2000
    assert check_correctness_of_products.quantity == 4


@pytest.fixture
def check_correct_init_number():
    return Category("Футболки", "Футболки - удобный предмет одежды", ['женские футболки', 'мужские футболки', 'детские футболки'])

def test_total_number(check_correct_init_number):
    assert check_correct_init_number.amount_of_unique_goods == 2
    assert check_correct_init_number.total_amount_of_categories == 1
"""Тесты."""

from src.main import Category


def test_product_init(init_product):
    assert init_product.name == "Iphone 15"
    assert init_product.description == "512GB, Gray space"
    assert init_product.price == 210000.0
    assert init_product.quantity == 8


def test_init_category(init_category):
    assert init_category.name == "Смартфоны"
    assert (
        init_category.description
        == "Смартфоны, как средство не только коммуникации, \
    но и получения дополнительных функций для удобства жизни"
    )
    assert init_category.products == []

    assert init_category.category_count == 1
    assert init_category.product_count == 0


def test_category_count(category):
    assert Category.category_count == 3


def test_product_count_with_products(category_prod):
    # Проверяем, что количество продуктов увеличилось
    assert Category.product_count == 4  # 3 в первой категории + 1 во второй категории


def test_product_count_without_products(without_products):
    # Проверяем, что количество продуктов остается 0
    assert Category.product_count == 0


def test_combined_category_and_product_count(combined_category_and_product):
    # Проверяем, что количество категорий и продуктов корректно
    assert Category.category_count == 2  # Две категории
    assert Category.product_count == 2  # Два продукта в первой категории

import pytest

from src.main import Category, Product


@pytest.fixture
def product():
    """Тестируем инициализацию Product."""
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def category():
    """Тестируем инициализацию Category."""
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, \
    но и получения дополнительных функций для удобства жизни",
    )


@pytest.fixture(autouse=True)
def reset_category_product_count():
    """Сбрасываем счетчики перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def category_1():
    """Создаем несколько категорий."""
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, \
        но и получения дополнительных функций для удобства жизни",
    )
    return category1


@pytest.fixture
def category_2():
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет \
        наслаждаться просмотром, станет вашим другом и помощником",
    )
    return category2


@pytest.fixture
def category_3():
    category3 = Category(
        "Телевизоры1",
        "Современный телевизор, который позволяет \
        наслаждаться просмотром, станет вашим другом и помощником",
    )
    return category3


@pytest.fixture
def category_prod():
    """Создаем продукты."""
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

    # Создаем категории с продуктами
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, \
        но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, \
        станет вашим другом и помощником",
        [product4],
    )
    return category1, category2


@pytest.fixture
def without_products():
    """Создаем категорию без продуктов."""
    category = Category("Без продуктов", "Пустая категория")
    return category


@pytest.fixture
def combined_category_and_product():
    """Создаем продукты."""
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    # Создаем категорию с продуктами
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения \
        дополнительных функций для удобства жизни",
        [product1, product2],
    )

    # Создаем еще одну категорию без продуктов
    category2 = Category("Без продуктов", "Пустая категория")
    return category1, category2

from src.category import Category


def test_category(category_phones, category_tv):
    assert category_phones.name == "Смартфоны"
    assert (
        category_phones.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category_phones.product_list) == 3
    assert category_tv.name == "Телевизоры"
    assert (
        category_tv.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert len(category_tv.product_list) == 1
    assert Category.category_count == 2
    assert Category.product_count == 4


def test_category_products_property(category_phones):
    assert category_phones.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_category_add_product(category_phones, product_test):
    assert len(category_phones.product_list) == 3
    category_phones.add_product(product_test)
    assert len(category_phones.product_list) == 4


def test_category_str(category_phones):
    assert str(category_phones) == "Смартфоны, количество продуктов: 27 шт."

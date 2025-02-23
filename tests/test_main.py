# from src.category import Category
# from src.product import Product
#
#
# def test_main_product(product_samsung, product_iphone, product_xiaomi):
#     assert product_samsung.name == "Samsung Galaxy S23 Ultra"
#     assert product_samsung.description == "256GB, Серый цвет, 200MP камера"
#     assert product_samsung.price == 180000.0
#     assert product_samsung.quantity == 5
#
#     assert product_iphone.name == "Iphone 15"
#     assert product_iphone.description == "512GB, Gray space"
#     assert product_iphone.price == 210000.0
#     assert product_iphone.quantity == 8
#
#     assert product_xiaomi.name == "Xiaomi Redmi Note 11"
#     assert product_xiaomi.description == "1024GB, Синий"
#     assert product_xiaomi.price == 31000.0
#     assert product_xiaomi.quantity == 14
#
#
# def test_main_category(category_phones, category_tv):
#     assert category_phones.name == "Смартфоны"
#     assert (
#         category_phones.description
#         == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
#     )
#     assert len(category_phones.product_list) == 3
#     assert category_tv.name == "Телевизоры"
#     assert (
#         category_tv.description
#         == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
#     )
#     assert len(category_tv.product_list) == 1
#     assert Category.category_count == 2
#     assert Category.product_count == 4
#
#
# def test_category_products_property(category_phones):
#     assert category_phones.products == (
#         "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
#         "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
#         "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
#     )
#
#
# def test_category_add_product(category_phones, product_samsung):
#     assert len(category_phones.product_list) == 3
#     category_phones.add_product(product_samsung)
#     assert len(category_phones.product_list) == 4
#
#
# def test_product_price_setter(capsys, product_iphone):
#     product_iphone.price = 0
#     message = capsys.readouterr()
#     assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
#     product_iphone.price = 210000.0
#     assert product_iphone.price == 210000.0

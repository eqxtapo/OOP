import pytest
from src.product import Product


def test_main_product(first_smartphone, second_smartphone, third_smartphone):
    assert first_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert first_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert first_smartphone.price == 180000.0
    assert first_smartphone.quantity == 5
    assert first_smartphone.efficiency == 95.5
    assert first_smartphone.model == "S23 Ultra"
    assert first_smartphone.memory == 256
    assert first_smartphone.color == "Серый"

    assert second_smartphone.name == "Iphone 15"
    assert second_smartphone.description == "512GB, Gray space"
    assert second_smartphone.price == 210000.0
    assert second_smartphone.quantity == 8
    assert second_smartphone.efficiency == 98.2
    assert second_smartphone.model == "15"
    assert second_smartphone.memory == 512
    assert second_smartphone.color == "Gray space"

    assert third_smartphone.name == "Xiaomi Redmi Note 11"
    assert third_smartphone.description == "1024GB, Синий"
    assert third_smartphone.price == 31000.0
    assert third_smartphone.quantity == 14
    assert third_smartphone.efficiency == 90.3
    assert third_smartphone.model == "Note 11"
    assert third_smartphone.memory == 1024
    assert third_smartphone.color == "Синий"


def test_product_price_setter(capsys, product_iphone):
    product_iphone.price = 0
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"
    product_iphone.price = 210000.0
    assert product_iphone.price == 210000.0


def test_product_str(product_xiaomi):
    assert str(product_xiaomi) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."


def test_product_add(product_samsung, product_iphone, product_xiaomi):
    assert product_samsung + product_iphone == 2580000
    assert product_samsung + product_xiaomi == 1334000
    assert product_xiaomi + product_iphone == 2114000


def test_fail_product_add(first_smartphone, grass):
    with pytest.raises(TypeError):
        assert first_smartphone + grass

def test_product_init_zero_quantity():
    with pytest.raises(ValueError):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)

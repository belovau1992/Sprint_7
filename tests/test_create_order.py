import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from create_courier_method import CreateCourierMethod
from urls import Urls


import requests
import allure
import pytest
from data import DataForOrder

class TestCreateOrder:
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    @allure.title("Создание заказа с цветом: {color}")
    def test_create_order_with_colors(self, color):
        body = DataForOrder.CREATE_ORDER_BODY.copy()
        body["color"] = color
        response = requests.post(f'{Urls.BASE_URL}{Urls.CREATE_ORDER_URL}', json=body)
        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title("Создание заказа без обязательных полей")
    @pytest.mark.parametrize("field", [
        "firstName", "lastName", "address",
        "metroStation", "phone", "rentTime",
        "deliveryDate", "comment"
    ])
    def test_missing_required_field(self, field):
        body = DataForOrder.CREATE_ORDER_BODY.copy()
        body.pop(field)
        response = requests.post(f'{Urls.BASE_URL}{Urls.CREATE_ORDER_URL}', json=body)
        assert response.status_code == 400
        assert "Недостаточно данных" in response.text

class TestGetOrders:
    @allure.title("Получение списка заказов")
    def test_get_orders_list(self):
        response = requests.get(f'{Urls.BASE_URL}{Urls.CREATE_ORDER_URL}')
        assert response.status_code == 200
        assert len(response.json()["orders"]) > 0  # Проверяем, что список не пустой
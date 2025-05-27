import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from create_courier_method import CreateCourierMethod
from data import DataForOrder
from urls import Urls

import allure
import pytest
from create_courier_method import CreateCourierMethod


class TestCreateCourier:
    @allure.title("Успешное создание курьера")
    def test_success_create_courier(self,generate_courier_body):
        with allure.step("Создание курьера"):
            response = CreateCourierMethod.create_courier(generate_courier_body)
        assert response.status_code == 201
        assert response.json()["ok"] is True

    @allure.title("Создание курьера с дублирующимся логином")
    def test_create_duplicate_courier_fails(self, generate_courier_body):
        # Сначала создаём курьера
        CreateCourierMethod.create_courier(generate_courier_body)

        # Пытаемся создать такого же ещё раз
        with allure.step("Попытка создать дубликат курьера"):
            duplicate_response = CreateCourierMethod.create_courier(generate_courier_body)

        assert duplicate_response.status_code == 409  # Конфликт
        assert "Этот логин уже используется" in duplicate_response.text

    @pytest.mark.parametrize("field", ["login", "password", "firstName"])
    @allure.title("Ошибка при отсутствии обязательного поля {field}")
    def test_missing_required_field(self, generate_courier_body, field):
        body = generate_courier_body.copy()
        body.pop(field)
        response = CreateCourierMethod.create_courier(body)
        assert response.status_code == 400
        assert "Недостаточно данных" in response.text

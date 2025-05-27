import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from create_courier_method import CreateCourierMethod
from data import DataForOrder


import allure
import pytest
import requests

from urls import Urls


class TestLoginCourier:
    @allure.title("Успешная авторизация курьера")
    def test_success_login(self, register_new_courier):
        login, password = register_new_courier[0], register_new_courier[1]
        payload = {"login": login, "password": password}
        response = requests.post(f'{Urls.BASE_URL}{Urls.LOGIN_URL}', json=payload)
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Ошибка при неверном пароле")
    def test_wrong_password_fails(self, register_new_courier):
        payload = {"login": register_new_courier[0], "password": "wrong"}
        response = requests.post(f'{Urls.BASE_URL}{Urls.LOGIN_URL}', json=payload)
        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.text

    @pytest.mark.parametrize("field", ["login", "password"])
    @allure.title("Ошибка при отсутствии поля {field}")
    def test_missing_field(self, register_new_courier, field):
        payload = {"login": register_new_courier[0], "password": register_new_courier[1]}
        payload.pop(field)
        response = requests.post(f'{Urls.BASE_URL}{Urls.LOGIN_URL}', json=payload)
        assert response.status_code == 400
        assert "Недостаточно данных" in response.text
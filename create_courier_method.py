import requests
from urls import Urls


class CreateCourierMethod:
    @staticmethod
    def create_courier(body):
        return requests.post(f'{Urls.BASE_URL}{Urls.CREATE_COURIER_URL}', json=body)
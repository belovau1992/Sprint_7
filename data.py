class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER_URL = '/api/v1/courier'
    CREATE_ORDER_URL = '/api/v1/orders'
    LOGIN_URL = '/api/v1/courier/login'
    GET_ORDER_BY_TRACK = '/api/v1/orders/track'  # + track number(например ?t=123456)

class DataForCourier:
    CREATE_COURIER_BODY = {
    "login": "ninja",
    "password": "1234",
    "firstName": "saske"
    }

class DataForLogin:
    LOGIN_BODY = {
    "login": "ninja",
    "password": "1234"
    }

class DataForOrder:
    CREATE_ORDER_BODY = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
    }
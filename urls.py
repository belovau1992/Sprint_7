class Urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER_URL = '/api/v1/courier'
    CREATE_ORDER_URL = '/api/v1/orders'
    LOGIN_URL = '/api/v1/courier/login'
    GET_ORDER_BY_TRACK = '/api/v1/orders/track'  # + track number(например ?t=123456)
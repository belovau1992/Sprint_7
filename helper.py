from data import DataForCourier
from data import DataForLogin
from data import DataForOrder

def modify_courier_body(key,value):
    body = DataForCourier.CREATE_COURIER_BODY.copy()
    body[key] = value
    return body

def modify_login_body(key,value):
    body = DataForLogin.LOGIN_BODY.copy()
    body[key] = value
    return body

def modify_order_body(key,value):
    body = DataForOrder.CREATE_ORDER_BODY.copy()
    body[key] = value
    return body
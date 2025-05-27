from faker import Faker

#генерация данных для создания заказа
fake = Faker("ru_RU")
def generate_order_body():
    return {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": fake.random_int(min=1, max=435),
        "phone": fake.phone_number(),
        "rentTime": fake.random_int(min=1, max=7),
        "deliveryDate": fake.date_between(start_date='today', end_date='+30d').isoformat(),
        "comment": fake.text(max_nb_chars=200),
        "color": [fake.random_element(["BLACK", "GREY"])]
    }
def generate_courier_body():
    return {
        "login": fake.user_name(),
        "password": fake.password(),
        "firstName": fake.first_name()
    }

def generate_login_body():
    return {
        "login": fake.user_name(),
        "password": fake.password()
    }
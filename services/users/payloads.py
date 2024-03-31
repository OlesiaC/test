from faker import Faker

fake = Faker()


class Payloads:
    create_user = {
        "username": fake.user_name(),
        "email": fake.email(),
    }
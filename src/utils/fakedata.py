import json
from faker import Faker

def fakedatacustomer(size: int = 1):
    fake = Faker()

    data = []

    for i in range(size):

        customer = {}
        customer['id'] = fake.random_int(min=10, max=50)
        customer['name'] = fake.name()
        customer['address'] = fake.address()
        customer['phone_number'] = fake.phone_number()
        customer['date_of_birth'] = fake.date()

        data.append(customer)

    return str(data)


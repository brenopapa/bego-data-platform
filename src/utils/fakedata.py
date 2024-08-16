import json, random
from faker import Faker

def fakedata(entity: str, size: int = 1):
    fake = Faker()

    data = []

    if entity == 'customer':
        for i in range(size):

            object = {}
            object['id'] = fake.random_int(min=1, max=10)
            object['name'] = fake.name()
            object['country'] = fake.country()
            object['phone_number'] = fake.phone_number()
            object['date_of_birth'] = fake.date()

            data.append(object)

        return str(data)

    if entity == 'product':
        for i in range(size):

            object = {}
            object['id'] = fake.random_int(min=1, max=20)
            object['name'] = random.choice(['Apple','Banana','Orange','Strawberry','Blueberry','Pineapple','Mango','Grapes','Kiwi','Watermelon','Peach','Pear','Plum','Cherry','Raspberry','Apricot','Pomegranate','Papaya'])

            data.append(object)

        return str(data)

    if entity == 'purchase':
        for i in range(size):

            object = {}
            object['id'] = fake.ean(length=8)
            object['customer_id'] =  fake.random_int(min=1, max=10)
            object['product_id'] = fake.random_int(min=1, max=20)
            object['value'] = fake.pricetag()
            object['date'] = fake.date()

            data.append(object)

        return str(data)
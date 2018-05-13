from models.customer import Customer
from faker import Faker
from random import randint, choice
import mlab

mlab.connect()

fake = Faker()

for i in range(50):
    print("Saving", i + 1, ".....")
    customer = Customer(name = fake.name(),
                        gender = randint(0,1),
                        email = fake.email(),
                        phone = fake.phone_number(),
                        job = fake.job(),
                        company = fake.company(),
                        contacted = choice([True, False])
    )


    customer.save()

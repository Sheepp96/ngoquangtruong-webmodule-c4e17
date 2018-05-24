from models.service import Service
from faker import Faker
from random import *
import mlab

mlab.connect()

fake = Faker()



for i in range(50):
    g = randint(0, 1)
    if g == 0:
        im = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcnqkEM05vfQ3l7foqsXi7QDOroEJ7R6h_TxRUEoX8774yYp2q"
    else:
        im = "http://thage.com/wp-content/uploads/2014/05/profile.png"

    descriptions = choice(['Ngoan hiền, dễ thương, lễ phép với gia đình', 'Cao to, đen hôi', 'Yêu màu tím, thích sự thuỷ chung'])

    v1 = randint(70, 100)
    v2 = randint(60, 90)
    v3 = randint(70, 100)
    sd3v = [v1,v2,v3]

    print("Saving service", i + 1, ".....")
    service = Service(name = fake.name(),
                      yob = randint(1990, 2001),
                      gender = g,
                      height = randint(155, 180),
                      phone = fake.phone_number(),
                      address = fake.address(),
                      description = descriptions,
                      measurements = sd3v,
                      image = im,
                      status = choice([True, False]))
    service.save()

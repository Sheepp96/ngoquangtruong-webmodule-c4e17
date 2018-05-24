# from mongoengine import *
#
# #design database
# #create collection
# class Service(Document):
#     name = StringField()
#     yob = IntField()
#     gender = IntField()
#     # weight = IntField()
#     height = IntField()
#     phone = StringField()
#     address = StringField()
#     status = BooleanField()


from mongoengine import *

class Service(Document):
    name         = StringField()
    yob          = IntField()
    gender       = IntField()
    height       = IntField()
    phone        = StringField()
    address      = StringField()
    status       = BooleanField()
    description  = StringField()
    measurements = ListField()
    image        = StringField()

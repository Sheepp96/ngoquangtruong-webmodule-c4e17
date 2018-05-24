import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds127139.mlab.com:27139/muadongkhonglanh-c4e17

host = "ds127139.mlab.com"
port = 27139
db_name = "muadongkhonglanh-c4e17"
user_name = "admin"
password = "admin"

#mongodb://<dbuser>:<dbpassword>@ds249798.mlab.com:49798/muadongkhonglanh

# host = "ds249798.mlab.com"
# port = 49798
# db_name = "muadongkhonglanh"
# user_name = "admin"
# password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())

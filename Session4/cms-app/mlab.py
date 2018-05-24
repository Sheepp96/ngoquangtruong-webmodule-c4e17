# mongodb://<dbuser>:<dbpassword>@ds263707.mlab.com:63707/cms-app

import mongoengine

host = "ds263707.mlab.com"
port = 63707
db_name = "cms-app"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())

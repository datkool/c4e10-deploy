import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds131312.mlab.com:31312/c4e10_dat

host = "ds131312.mlab.com"
port = 31312
db_name = "c4e10_dat"
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
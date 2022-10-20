import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"


def getData(id=None):
    data = {}
    if id is not None:
        data = {'id': id}

    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)


# getData(2)

def postData():
    data = {
        'name': 'shakeeb',
        'roll': 104,
        'city': 'Multan'
    }

    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)


# postData()


def updateData():
    data = {
        'id': 2,
        'name': 'Maryam',
        'city': 'Lahore'
    }

    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)


# updateData()


def deleteData():
    data = {'id': 2}

    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)


deleteData()

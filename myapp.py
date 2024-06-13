import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

#FE for get request (Read)
def get_data(id = None):
    data = {}   
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)

    req = requests.get(url = URL, data = json_data)
    data = req.json()
    print(data)

# get_data()  

#FE for post request(Create)
def post_data():
    data = {
        'id': 7,
        'name': 'anurag',
        'roll_no': 109,
        'course': 'Medical billing',
        'city': 'indirapuram'
    }

    json_data = json.dumps(data)
    req = requests.post(url = URL, data = json_data)
    data = req.json()
    print(data)

# post_data()

def update():
    data = {
        'id': 3,
        'course': 'digi marketing',

    }
    json_data = json.dumps(data)
    req = requests.put(url = URL, data = json_data)
    data = req.json()
    print(data)

# update()

def delete():
    data = {'id': 2 }
    json_data = json.dumps(data)
    req = requests.delete(url = URL, data=json_data)
    data = req.json()
    print(data)

delete()


    
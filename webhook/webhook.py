import requests
import json

webhook_url = 'http://127.0.0.1:5000/webhook'

data = {
    'name': 'Kwame',
    'age': 16,
    'is_human': True
}

data_json = json.dumps(data)

r = requests.post(webhook_url, data=data_json, headers={'Content-Type': 'application/json'})

print("Data sent successful!!!")


                                                        
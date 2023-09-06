import requests
import json

webhook_url = "http://127.0.0.1:5000/webhook"

data = {
    'name': 'Kwame',
    'age': 16,
    'is_human': True
}

data_json = json.dumps(data)

response = requests.post(data=data_json, headers={'Content-Type': 'application/json'})

if response.status_code == 200:
    print("Data sent successfully!!!")

if response.status_code == 404:
    print("Data failed ")
else:
    print("Something wen't wrong")   
    

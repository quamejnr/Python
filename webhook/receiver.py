from flask import Flask, request
import requests

app = Flask(__name__)    

# def get_country(ip_address):
#     response = requests.get("http://ip-api.com/json/{}".format(ip_address))
#     return response.json()

# @app.route('/webhook', methods=['POST'])
# def webhook():
#     ip_address = request.remote_addr
#     print(ip_address)
#     print(get_country(ip_address))
#     # print(request.json)
#     return 'success', 200

data = {
    "games": [
    	{"id": 1, "title": "Horizon: Zero Dawn", "genre": "Action", "platform": "PS4", "year": "2017", "price": 250.00},
        {"id": 2, "title": "God of War", "genre": "Adventure", "platform": "PS4", "year": "2018", "price": 250.00},
        {"id": 3, "title": "Spiderman: Miles Morales, Ultimate Edition", "genre": "Action", "platform": "PS5", "year": "2022", "price": 700.00},
        {"id": 4, "title": "Horizon: Forbidden West", "genre": "Action", "platform": "PS5", "year": "2022", "price": 550.00},
    ]
}
    

@app.route('/games', methods=['GET'])
def getGames():
    return data

if __name__ == '__main__':
    app.run()
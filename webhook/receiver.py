from flask import Flask, request


app = Flask(__name__)
    
    
@app.route('/webhook', methods=['POST'])
def webhook():
    print(request.json)
    return 'success', 200
    

if __name__ == '__main__':
    app.run()
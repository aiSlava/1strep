from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    
    # Обробка отриманих даних
    print(f"Received data: {data}")
    
    # Відправлення даних у Make
    make_url = "https://hook.eu2.make.com/t7w4h963aacihxv90w3973tubf929yv3"
    response = requests.post(make_url, json=data)
    
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

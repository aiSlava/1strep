import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Маршрут для обробки запитів
@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Отримуємо дані з запиту
        data = request.json
        print(f"Received data: {data}")  # Лог отриманих даних

        # URL Webhook з Make
        make_url = "https://hook.eu2.make.com/r1hgwm4jz9dffhus0a436dqrv3mkt7b8"

        # Відправляємо дані до Make
        response = requests.post(make_url, json=data)
        print(f"Response from Make: {response.status_code}, {response.text}")  # Лог відповіді від Make

        # Повертаємо відповідь
        return jsonify({"status": "success", "make_response": response.text}), response.status_code
    except Exception as e:
        # Логування помилок
        print(f"Error occurred: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

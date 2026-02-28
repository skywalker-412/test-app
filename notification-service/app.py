from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    # Simulate sending notification (email/SMS)
    user = data.get('user')
    message = data.get('message')
    # Here you would integrate with an email/SMS provider
    return jsonify({'status': 'sent', 'user': user, 'message': message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)

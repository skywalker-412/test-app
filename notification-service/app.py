from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)


# UI homepage
@app.route('/', methods=['GET'])
def home():
    html = '''
    <h2>Notification Service</h2>
    <p>Use <b>/notify</b> (POST) to send a notification.</p>
    <p>This service simulates sending notifications.<br>
    Example payload:<br>
    <code>{"user": "test", "message": "Hello!"}</code></p>
    '''
    return render_template_string(html)

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    user = data.get('user')
    message = data.get('message')
    return jsonify({'status': 'sent', 'user': user, 'message': message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)

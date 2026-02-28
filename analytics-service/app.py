from flask import Flask, request, jsonify

app = Flask(__name__)

analytics_data = []

@app.route('/track', methods=['POST'])
def track():
    data = request.json
    analytics_data.append(data)
    return jsonify({'status': 'tracked', 'data': data})

@app.route('/report', methods=['GET'])
def report():
    return jsonify({'analytics': analytics_data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)

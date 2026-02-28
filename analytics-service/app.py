from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

analytics_data = []


# UI homepage
@app.route('/', methods=['GET'])
def home():
    html = '''
    <h2>Analytics Service</h2>
    <p>Use <b>/report</b> to view analytics data.<br>
    Use <b>/track</b> (POST) to add data.</p>
    <p>Example: <a href="/report">View Report</a></p>
    '''
    return render_template_string(html)

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

from flask import Flask, jsonify, send_from_directory, request

app = Flask(__name__, static_folder='frontend', static_url_path='/')

# API route to send data to the Vue frontend
@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify({'message': 'Hello from Flask!'})

@app.route('/api/report', methods=['POST'])
def insert_message():
    report_json = request.get_json()
    for col in report_json:
        print(report_json[col])    
    return jsonify({"message":"success"})
# Route to serve the Vue app
    
# Catch-all route to serve the Vue app for client-side routing
@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import ssl

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_label', methods=['POST'])
def update_label():
    data = request.get_json()
    text_value = data.get('text', '')
    return jsonify({'message': text_value})

if __name__ == '__main__':
    # Create SSL context for HTTPS
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('cert.pem', 'key.pem')
    
    app.run(debug=True, host='0.0.0.0', port=5000, ssl_context=context)

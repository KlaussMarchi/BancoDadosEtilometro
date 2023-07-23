import socket, os, time 
from flask import Flask, jsonify, request, send_file 
from flask_cors import CORS
import pandas as pd 

app = Flask(__name__) 
CORS(app)  # habilitar CORS

@app.route('/version')
def handle_get_1():
    return '5.2.0'

@app.route('/sensorID', methods=['POST'])
def handle_post_1():
    data = request.data.decode('utf-8')

    if data == 'MQ3':
        return 'OK'
    
    return 'NOT OK'

@app.route('/espID', methods=['POST'])
def handle_post_2():
    data = request.data.decode('utf-8')

    if data == 'ESP32':
        return 'OK'
    
    return 'NOT OK'

@app.route('/download', methods=['GET'])
def download_file():
    return send_file('Teste.xlsx', as_attachment=True)

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

if __name__ == '__main__':
    print()
    print(f"IP: http://{get_ip_address()}:5000")
    print()

    app.run(host='0.0.0.0', port=5000)

from flask import Flask, jsonify, request
import random
import time
from prometheus_client import start_http_server, Gauge, generate_latest

app = Flask(__name__)

heart_rate_gauge = Gauge('heart_rate', 'Heart rate in beats per minute')
blood_pressure_gauge = Gauge('blood_pressure', 'Blood pressure in mmHg')

def generate_health_data():
    heart_rate = random.randint(60, 100)  
    systolic_bp = random.randint(110, 140)  
    diastolic_bp = random.randint(70, 90)  
    return heart_rate, systolic_bp, diastolic_bp

@app.route('/health-data', methods=['GET'])
def get_health_data():
    heart_rate, systolic_bp, diastolic_bp = generate_health_data()
    return jsonify({
        "heart_rate": heart_rate,
        "blood_pressure": {
            "systolic": systolic_bp,
            "diastolic": diastolic_bp
        }
    })

@app.route('/metrics', methods=['GET'])
def metrics():
    heart_rate, systolic_bp, diastolic_bp = generate_health_data()
    
  
    heart_rate_gauge.set(heart_rate)
    blood_pressure_gauge.set(systolic_bp)  
    
   
    return generate_latest()

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    start_http_server(5001)  
    app.run(host="0.0.0.0", port=5001)  

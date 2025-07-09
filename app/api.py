from app import reservations
from flask import Flask, jsonify, request
from app.reservations import check_availability

app = Flask(__name__)

reservations = []

@app.route('/reservations', methods=['POST'])
def create_reservations():
    data = request.get_json()
    is_available = check_availability(reservations, data) 


    if is_available:
        reservations.append(data)
        return jsonify({"message": "Successfully reserved"}), 201
    else:
        return jsonify({"message": "Room is not available"}), 409
from flask import Blueprint, jsonify, request


apicreate = Blueprint('apicreate', __name__)

@apicreate.route('/api/create', methods=['POST'])
def create():
    data = request.get_json()
    return jsonify(data), 201
    if not data:
        return jsonify({'message': 'No data provided'}), 400
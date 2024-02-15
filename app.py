from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data - imagine it comes from a database
users = [
    {"id": 1, "username": "john"},
    {"id": 2, "username": "jane"},
    {"id": 3, "username": "alice"}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if 'username' not in data:
        return jsonify({'error': 'Username is required'}), 400
    user = {
        'id': len(users) + 1,
        'username': data['username']
    }
    users.append(user)
    return jsonify(user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    data = request.json
    if 'username' not in data:
        return jsonify({'error': 'Username is required'}), 400
    user['username'] = data['username']
    return jsonify(user)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user['id'] != user_id]
    return jsonify({'message': 'User deleted'})

if __name__ == '__main__':
    app.run(debug=True)

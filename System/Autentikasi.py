from flask import Flask, request, jsonify
import bcrypt


// author : hafizhhasyhari
// github : @hafizhhasyhari

app = Flask(__name__)

# Simulasi database
users_db = {}

@app.route('/register', methods=['POST'])
def register():
    username = request.json['username']
    password = request.json['password'].encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    users_db[username] = hashed
    return jsonify({"message": "User registered successfully!"}), 201

@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password'].encode('utf-8')
    
    if username in users_db and bcrypt.checkpw(password, users_db[username]):
        return jsonify({"message": "Login successful!"}), 200
    return jsonify({"message": "Invalid credentials!"}), 401

if __name__ == '__main__':
    app.run(debug=True)

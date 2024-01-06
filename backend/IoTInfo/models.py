from flask import Flask, jsonify
from sqlalchemy.exc import IntegrityError
from flask import Blueprint

auth = Blueprint('auth', __name__)

app = Flask(__name__)
app.register_blueprint(auth)

@auth.route('/login')
def login():
    return "Login page"

@app.route('/add_device', methods=['POST'])
def add_device():
    data = request.get_json()
    MACaddress = data['MACaddress']
    iotname = data['iotname']
    username = data['username']
    password = data['password']
    
    # デバイスを追加する際のエラー処理
    try:
        return jsonify({"message": "Device added successfully."}), 200
        # デバイスの追加を試みる（iotnameが一意であることが必要）
    except IntegrityError:
        # 一意性制約違反が発生した場合、エラーレスポンスを返す
        return jsonify({"error": "A device with this name already exists."}), 400
    
@app.route('/get_devices', methods=['GET'])
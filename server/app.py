from flask import Flask,request
from flask_cors import CORS
import json
from time import sleep

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    res = {"status":"hello"}
    return json.dumps(res)

@app.route('/user',methods=['POST'])#POST
def create_user():
    username = request.form['username']
    password = request.form['password']
    print('username',username)
    print('password',password)
    sleep(1.5)
    return json.dumps({"status":"create user success","user":username})


if __name__ == "__main__":
    app.run(debug=True)
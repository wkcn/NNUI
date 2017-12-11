from flask import Flask, request, jsonify
import json
from executor import new_model
app = Flask(__name__)

@app.route('/get/')
def get_res():
    username = request.args.get('usr')
    if(username != ''):
        print('received parameter usr:',username)

    password = request.args.get('pwd')
    if(password != ''):
        print('received parameter pwd:',password)

    jsonpack = request.json
    print('This is json message :', jsonpack,'\n\n')
    return jsonify(jsonpack)
    
@app.route('/post', methods = ['POST'])
def post_res():
    jsonpack = request.json
    # the type of jsonpack is dict
    print('This is json message :', jsonpack, '\n\n')
    mid = new_model(jsonpack)
    result = {
        "id": mid
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, use_debugger=True)
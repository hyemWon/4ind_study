from flask import Flask, jsonify, make_response, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET','POST','PUT','DELETE'])
def test():
    if request.method == 'POST':
        print('POST')
        data = request.get_json()
        print(data['email'])
    if request.method == 'GET':
        print('GET')
        user = request.args.get('email')
        print(user)
    if request.method == 'PUT':
        print('PUT')
        user = request.args.get('email')
        print('user')
    if request.method == 'DELETE':
        print('DELETE')
        user = request.args.get('email')
        print(user)

    # return make_response(jsonify(suceesss=True), 200)
    return make_response(jsonify({'status': True}), 200)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
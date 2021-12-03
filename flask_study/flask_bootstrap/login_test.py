# backend

from flask import Flask, jsonify, request, render_template

# static path 옵션 (모든 다른 파일들은 static에 넣겠다)
app = Flask(__name__, static_url_path='/static')

@app.route('/login')
def login():
    email = request.args.get('user_email')
    password = request.args.get('user_pw')
    print(email, password)

    if email == 'alrema@naver.com':
        return_data = {'auth': 'success'}
    else:
        return_data = {'auth': 'failed'}

    return jsonify(return_data)


@app.route('/html_test')
def hello_html():
    return render_template('login_rawtest.html')


if __name__=="__main__":
    app.run(host='localhost', port=8080)
# before_first_request : 웹 application 기동 이후 가장 처음에 들어오는 HTTP 요청에서만 실행
# before_request : HTTP 요청이 들어올 때마다 실행 (해당 요청 실행 전에 먼저 들어옴)
# 위 두개는 인자 전달이 안됨
# after_ request: HTTP 요청 처리가 끝나고 브라우저에 응답하기 전에 실행 (response를 리턴해야 함)

from flask import Flask
import requests

app = Flask(__name__)

@app.before_first_request
def before_first_request():
    print("flask 실행 후 첫 요청 때만 실행")

@app.before_request
def before_request():
    print("HTTP 요청이 들어올 때마다 실행")

@app.after_request
def after_request(response):
    print("HTTP 요청 처리가 끝나고 브라우저에 응답하기 전에 실행")
    return response


@app.route("/hello")
def hello():
    print("hello")
    return "<h1>Hello Flask!</h1>"


if __name__=='__main__':
    app.run('0.0.0.0', port='8080')
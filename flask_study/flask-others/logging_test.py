from flask import Flask

app = Flask(__name__)


# 상용화시에는 app.debug를 False로 놓고, 디버그 정보를 로그로 남기는 것이 일반적임
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler # 사용할 logging 핸들러 이름
    file_handler = RotatingFileHandler('helena.server.log', maxBytes=2000, backupCount=10)
    file_handler.setLevel(logging.WARNING) # 어느 단계까지 로깅을 할지
    app.logger.addHandler(file_handler) # app.logger.addHandler()에 등록시켜줘야 app.logger로 사용가능


@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return "<h1>해당 경로에 맞는 웹페이지가 없습니다. 문제가 지속되면, 관리자에게 연락해주세요.</h1>", 404


if __name__=='__main__':
    app.run(host='0.0.0.0', port='8080', debug=False)

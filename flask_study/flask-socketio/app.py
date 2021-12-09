from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'siri' # 암호화
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route('/')
def sessions():
    return render_template('session.html')

def receive_message(methods=['GET','POST']):
    print('message was received!!!')


# 클라이언트에서 websocket 메시지를 수신하기 위해 이벤트 핸들러 정의
@socketio.on( 'my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit( 'my response', json, callback=receive_message) # send() / emit() 사용하여 연결된 클라이언트에 응답 메시지 보냄
    


if __name__=='__main__':
    socketio.run(app,host='localhost', port='5000', debug=True)


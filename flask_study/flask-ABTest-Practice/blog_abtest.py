from flask import Flask, jsonify, request, render_template, make_response
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import CORS
# 동일 웹서버에서는 괜찮은데, 다른 웹서버로의 스크립트를 통한 접속/통신할때 CORS 필요
from blog_view import blog
import os

# https 만을 지원하는 기능을 http에서 테스트할 때 필요한 설정
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# html파일에서 가져올 데이터는 전부 static 폴더에서 가져와라
app = Flask(__name__, static_url_path='/static')
CORS(app)
app.secret_key = 'helena_server' # flask login과 관련된 기능
# app.secure_key = 'helena_server'_# flask login과 관련된 기능

app.register_blueprint(blog.blog_abtest, url_prefix='/blog')

login_manager = LoginManager()
login_manager.init_app(app) # login manager에 app 등록
login_manager.session_protection = 'strong' # 세션을 보다 복잡하게 만듬

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id) # mysql에서 해당 id를 가지고 해당 유저의 객체 리턴

# 로그인 안된 사용자가 로그인된 사용자가 접근가능한 API를 호출했을 때 에러
@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False), 401)



if __name__=='__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)
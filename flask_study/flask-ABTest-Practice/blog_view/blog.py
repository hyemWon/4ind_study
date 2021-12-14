from flask import Flask, Blueprint, request, render_template, jsonify, make_response
from flask import redirect, url_for


blog_abtest = Blueprint('blog', __name__)

@blog_abtest.route('/set_email', methods=['GET','POST'])
def set_email():
    if request.method == 'GET':
        print('set_email', request.headers)  
        email = request.args.get('user_email')
        print(email)
        return redirect(url_for('blog.test_blog'))
    else:
        # print('set_email', request.headers)    
        # print('set_email', request.get_json())  # Rest API의 경우 대부분 json 형태이기 때문에 이 방식
        print('set_email', request.form) # input 타입의 경우
        print('set_email', request.form.get('user_email'))
        return redirect(url_for('blog.test_blog'))

    # return make_response(jsonify(success=True), 200)
    # return redirect("/blog/test_blog")
    


@blog_abtest.route('/test')
def test_blog():
    return render_template('blog_A.html')
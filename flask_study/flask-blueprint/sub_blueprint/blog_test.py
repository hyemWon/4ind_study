from flask import Blueprint

blog_ab = Blueprint('bp', __name__)

# http://localhost:8080/blog/blog1
@blog_ab.route('/blog1')
def blog():
    return "TEST BLUEPRINT"

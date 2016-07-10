from flask import render_template
from flask import Blueprint

api_login_view = Blueprint('api_login_view', __name__)


# 显示登录界面的函数  GET
@api_login_view.route('/login')
def login_view():
    return render_template('login.html')
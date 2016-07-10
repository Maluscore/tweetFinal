from flask import session
from models import User
from flask import redirect
from flask import url_for
from functools import wraps


# 通过 session 来获取当前登录的用户
def current_user():
    try:
        # print('session, debug', session.permanent)
        username = session.get('username', '')
        u = User.query.filter_by(username=username).first()
        return u
    except KeyError:
        return None


# 判断登录权限
def requires_login(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        # f 是被装饰的函数
        # 所以下面两行会先于被装饰的函数内容调用
        print('debug, requires_login')
        if current_user() is None:
            return redirect(url_for('api_login_view.login_view'))
        return f(*args, **kwargs)
    return wrapped

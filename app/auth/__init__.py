from flask import request
from flask import redirect
from flask import url_for
from flask import render_template
from flask import jsonify
from flask import session
from flask import Blueprint
from functools import wraps

from ..models import User

# blue 用来给 app 导入, 在本文件中添加路由函数
# auth 是 name, 用来给 url_for 提供路由函数
blue = Blueprint('auth', __name__)


# 通过 session 来获取当前登录的用户
def current_user():
    # print('session, debug', session.permanent)
    username = session.get('username', '')
    u = User.query.filter_by(username=username).first()
    return u


# 判断登录权限
def requires_login(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        # f 是被装饰的函数
        # 所以下面两行会先于被装饰的函数内容调用
        print('debug, requires_login')
        if current_user() is None:
            return redirect(url_for('login_view'))
        return f(*args, **kwargs)
    return wrapped


@blue.route('/')
def index():
    view = 'auth.login_view'
    # 由于是在相同蓝图下, 所以也可以这样写, 省略前缀
    # view = '.login_view'
    return redirect(url_for(view))


# 显示登录界面的函数  GET
@blue.route('/login')
def login_view():
    return render_template('login.html')


@blue.route('/register', methods=['POST'])
def register():
    print('register')
    form = request.get_json()
    u = User(form)
    print('register 2')
    r = {
        'success': True
    }
    status, msgs = u.register_validate()
    if status:
        print("register success", form)
        # 保存到数据库
        u.gid = 10
        u.save()
        r['next'] = request.args.get('next', url_for('controllers.timeline_view', user_id=u.id))
        session.permanent = True
        session['username'] = u.username
    else:
        print('register failed', form)
        r['success'] = False
        r['message'] = '\n'.join(msgs)
    return jsonify(r)


# 处理登录请求  POST
@blue.route('/login', methods=['POST'])
def login():
    form = request.get_json()
    username = form.get('username', '')
    user = User.user_by_name(username)

    print('user login', user, form)
    r = {
        'success': False,
        'message': '登录失败',
    }
    if user is not None and user.validate_auth(form):
        r['success'] = True
        r['next'] = request.args.get('next', url_for('controllers.timeline_view', user_id=user.id))
        session.permanent = True
        session['username'] = username
    else:
        r['success'] = False
        r['message'] = '登录失败'
    return jsonify(r)


# 处理注销请求 POST
@blue.route('/logoff')
@requires_login
def logoff():
    session.pop('username')
    return redirect(url_for('.login_view'))

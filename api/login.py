from flask import Blueprint
from flask import request
from flask import url_for
from flask import jsonify
from flask import session
from models import User
from models import ResponseData


_author = 'peng'


api_login = Blueprint('api_login', __name__)


@api_login.route('/login', methods=['POST'])
def login():
    # u = User(request.form)
    form = request.get_json()
    username = form.get('username', '')
    user = User.query.filter_by(username=username).first()
    # r = {
    #     'success': False,
    #     'message': '登录失败',
    #     'next': '',
    # }
    r = ResponseData()
    if user is not None and user.validate_auth(form):
        r.success = True
        r.message = '登录成功'
        r.next = url_for('api_timeline.timeline_view', user_id=user.id)
        session.permanent = False
        session['username'] = username
    else:
        r.message = '登录失败'
    r = r.jsonstr()
    # print("r is ,", r)
    return jsonify(r)

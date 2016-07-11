from flask import request
from flask import session
from flask import url_for
from flask import jsonify
from flask import Blueprint

from models import User
from models import ResponseData

api_register = Blueprint('api_register', __name__)


# 处理注册的请求  POST
@api_register.route('/register', methods=['POST'])
def register():
    form = request.get_json()
    # print('debug, ', form)
    u = User(form)
    # print('debug, ', u)
    # r = {
    # }
    r = ResponseData()
    status, msgs = u.valid()
    if status:
        u.save()
        r.success = True
        r.next = url_for('api_timeline.timeline_view', user_id=u.id)
        # 下面这句可以在关闭浏览器后保持用户登录
        session.permanent = True
        session['username'] = u.username
    else:
        r.message = '\n'.join(msgs)
    r = r.jsonstr()
    print("r is ,", r)
    return jsonify(r)
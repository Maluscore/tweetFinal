from ..models import Follow
from ..models import User
from . import main
from . import current_user

from flask import request
from flask import jsonify


# 处理 关注用户 的请求 GET
@main.route('/follow', methods=['POST'])
def follow_act():
    form = request.get_json()
    user_now = current_user()
    f = Follow()
    f.user_id = user_now.id
    f.followed_id = form['id']
    f.save()
    r = {
        'success': True,
        'message': '关注成功！'
    }
    return jsonify(r)
    # return redirect(url_for('timeline_view', username=u.username))


# 处理 取消关注 的请求 GET
@main.route('/unfollow', methods=['POST'])
def unfollow_act():
    form = request.get_json()
    user_id = form['id']
    user_now = current_user()
    f = Follow().query.filter_by(user_id=user_now.id, followed_id=user_id).first()
    f.delete()
    # return redirect(url_for('timeline_view', username=u.username))

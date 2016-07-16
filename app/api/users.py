from ..models import Follow
from ..models import User
from . import main
from . import current_user
from flask import redirect
from flask import url_for


# 处理 关注用户 的请求 GET
@main.route('/follow/<user_id>')
def follow_act(user_id):
    user_now = current_user()
    u = User.query.filter_by(id=user_id).first()
    f = Follow()
    f.user_id = user_now.id
    f.followed_id = user_id
    f.save()
    fan_follow_count(user_now)
    return redirect(url_for('timeline_view', username=u.username))


# 处理 取消关注 的请求 GET
@main.route('/unfollow/<user_id>')
def unfollow_act(user_id):
    user_now = current_user()
    u = User.query.filter_by(id=user_id).first()
    f = Follow().query.filter_by(user_id=user_now.id, followed_id=user_id).first()
    f.delete()
    fan_follow_count(user_now)
    return redirect(url_for('timeline_view', username=u.username))

from flask import render_template
from flask import session
from flask import Blueprint

from ..models import User
from ..models import Follow


main = Blueprint('controllers', __name__)


# 通过 session 来获取当前登录的用户
def current_user():
    # print('session, debug', session.permanent)
    username = session.get('username', '')
    u = User.query.filter_by(username=username).first()
    return u


@main.route('/timeline/<user_id>')
def timeline_view(user_id):
    u = User.query.filter_by(id=user_id).first_or_404()
    follow_count = Follow.follow_count(u.id)
    fans = Follow.fans(u.id)
    tweets = [t for t in u.tweets if t.deleted == 0]
    tweets.sort(key=lambda t: t.created_time, reverse=True)
    d = dict(
        user=u,
        tweets=tweets,
        follows_count=len(follow_count),
        fans_count=len(fans),
    )
    return render_template('timeline.html', **d)


@main.route('/user/all')
def user_all():
    users = User.query.all()
    user = current_user()
    d = dict(
        user_all=users,
        current_user=user,
    )
    return render_template('user_all.html', **d)


@main.route('/user/<user_id>')
def user_view(user_id):
    u = User.query.filter_by(id=user_id).first()
    user = current_user()
    if u.id in Follow.follow_count(user.id):
        status = '取消关注'
    else:
        status = '关注'
    follow_count = Follow.follow_count(u.id)
    fans = Follow.fans(u.id)
    tweets = [t for t in u.tweets if t.deleted == 0]
    d = dict(
        user=u,
        tweets=tweets,
        current_user=user,
        status=status,
        follows_count=len(follow_count),
        fans_count=len(fans),
    )
    return render_template('user.html', **d)


# 显示 关注列表 的界面 GET
@main.route('/follow/list/<user_id>')
def follow_view(user_id):
    user_now = current_user()
    user = User.query.filter_by(id=user_id).first()
    follow_id = Follow.follow_count(user_id)
    follow_users = []
    for i in follow_id:
        follow_users.append(User.query.filter_by(id=i).first())
    follow_users.sort(key=lambda t: t.created_time, reverse=True)
    d = dict(
        user_now=user_now,
        follow_users=follow_users,
        user=user
    )
    return render_template('follow_users.html', **d)


# 显示 粉丝列表 的界面 GET
@main.route('/fan/list/<user_id>')
def fan_view(user_id):
    user_now = current_user()
    user = User.query.filter_by(id=user_id).first()
    all_fans = Follow.fans(user_id)
    all_fans.sort(key=lambda t: t.created_time, reverse=True)
    d = dict(
        user_now=user_now,
        all_fans=all_fans,
        user=user,
    )
    return render_template('fan_users.html', **d)
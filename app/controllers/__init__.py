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
    tweets = [t for t in u.tweets if t.deleted == 0]
    tweets.sort(key=lambda t: t.created_time, reverse=True)
    return render_template('timeline.html', user=u, tweets=tweets)


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
    tweets = [t for t in u.tweets if t.deleted == 0]
    d = dict(
        user=u,
        tweets=tweets,
        current_user=user,
    )
    return render_template('user.html', **d)


# 显示 关注列表 的界面 GET
@main.route('/follow/list/<user_id>')
def follow_view(user_id):
    user_now = current_user()
    user = User.query.filter_by(id=user_id).first()
    all_follows = Follow.query.filter_by(user_id=user_id).all()
    follow_users_id = [x.followed_id for x in all_follows]
    follow_users = []
    for i in follow_users_id:
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
    all_fans = Follow.query.filter_by(followed_id=user_id).all()
    fan_users = [x.follows for x in all_fans]
    fan_users.sort(key=lambda t: t.created_time, reverse=True)
    d = dict(
        user_now=user_now,
        fan_users=fan_users,
        user=user,
    )
    return render_template('fan_users.html', **d)
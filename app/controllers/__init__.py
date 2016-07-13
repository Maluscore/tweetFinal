from flask import render_template
from flask import session
from flask import Blueprint

from ..models import User


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
    tweets = u.tweets
    tweets.sort(key=lambda t: t.created_time, reverse=True)
    return render_template('timeline.html', user=u, tweets=tweets)

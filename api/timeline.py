from flask import render_template
from flask import Blueprint
from models import User

api_timeline = Blueprint('api_timeline', __name__)


@api_timeline.route('/timeline/<user_id>')
def timeline_view(user_id):
    user = User.query.filter_by(id=user_id).first()
    tweets = user.tweets
    tweets.sort(key=lambda t: t.created_time, reverse=True)
    return render_template('timeline.html', user=user, tweets=tweets)
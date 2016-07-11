from flask import render_template
from flask import Blueprint
from api.user_limit import requires_login

from models import User

api_timeline = Blueprint('api_timeline', __name__)


@api_timeline.route('/timeline/<user_id>')
@requires_login
def timeline_view(user_id):
    user = User.query.filter_by(id=user_id).first()
    return render_template('timeline.html', user=user)
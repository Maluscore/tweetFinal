from flask import render_template
from flask import Blueprint
from api.user_limit import requires_login
api_timeline = Blueprint('api_timeline', __name__)


@api_timeline.route('/timeline/<user_id>')
@requires_login
def timeline_view(user_id):
    return render_template('timeline.html', user_id=user_id)
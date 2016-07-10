from flask import request
from flask import jsonify
from flask import Blueprint

from models import Tweet
from models import ResponseData
from api.user_limit import current_user

api_tweet_add = Blueprint('api_tweet_add', __name__)


@api_tweet_add.route('/post/tweet/add', methods=['POST'])
def tweet_add():
    form = request.get_json()
    tweet = Tweet(form)
    u = current_user()
    tweet.user_id = u.id
    r = ResponseData()
    content = tweet.content
    if content is not None:
        tweet.save()
        r.message = '发表成功'
        r.content = content
        r.success = True
    else:
        r.message = '请输入有效内容'
    r = r.jsonstr()
    return jsonify(r)

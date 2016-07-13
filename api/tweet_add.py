from flask import Blueprint
from flask import jsonify
from flask import request

from api.user_limit import current_user
from app.api.time_filter import formatted_time
from models import ResponseData
from models import Tweet

api_tweet_add = Blueprint('api_tweet_add', __name__)


@api_tweet_add.route('/post/tweet/add', methods=['POST'])
def tweet_add():
    form = request.get_json()
    tweet = Tweet(form)
    u = current_user()
    tweet.user_id = u.id
    r = ResponseData()
    content = tweet.content
    # print('len, ', len(content)) 等于0
    # print('debug cc,', type(content)) 这里居然是字符串，看来ajax不会传null，空的直接当成空格了？
    if len(content) >= 1:
        tweet.save()
        r.message = '发表成功'
        r.success = True
        r = r.jsonstr()
        # 下面不能用等号去接，不然就是空
        r.update(u.json())
        # print('debug r,', r)
        r.update(tweet.json())
        r['created_time'] = formatted_time(tweet.created_time)
    else:
        r.message = '请输入有效内容'
        r = r.jsonstr()
    print(r)
    return jsonify(r)

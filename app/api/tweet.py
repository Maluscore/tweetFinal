from ..models import User
from ..models import Tweet
from . import main
from . import current_user

from flask import request
from flask import jsonify


@main.route('/tweet/add', methods=['POST'])
def tweet_add():
    form = request.get_json()
    tweet = Tweet(form)
    u = current_user()
    tweet.user_id = u.id
    content = tweet.content
    # print('len, ', len(content)) 等于0
    # print('debug cc,', type(content)) 这里居然是字符串，看来ajax不会传null，空的直接当成空格了？
    r = dict(
        success=False,
    )
    if len(content) >= 1:
        tweet.save()
        r['message'] = '发表成功'
        r['success'] = True
        # 下面不能用等号去接，不然就是空
        r['data'] = tweet.json()
    else:
        r['message'] = '请输入有效内容'
    print(r)
    return jsonify(r)

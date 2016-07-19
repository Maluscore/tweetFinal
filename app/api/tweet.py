from ..models import User
from ..models import Tweet
from . import main
from . import current_user
from ..time_filter import formatted_time

from flask import request
from flask import jsonify


@main.route('/tweet/add', methods=['POST'])
def tweet_add():
    form = request.get_json()
    tweet = Tweet(form)
    u = current_user()
    tweet.user_id = u.id
    tweet.sender_name = u.username
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
        r['data']['username'] = u.username
        r['data']['created_time'] = formatted_time(tweet.created_time)
    else:
        r['message'] = '请输入有效内容'
    print(r)
    return jsonify(r)


@main.route('/tweet/delete', methods=['POST'])
def tweet_delete():
    form = request.get_json()
    # print('debug form, ', form)
    t = Tweet.query.filter_by(id=form['id']).first()
    r = dict(
        success=True,
        message='去除成功！'
    )
    print('debug t,', t.deleted)
    if current_user().id == t.user_id:
        t.deleted = 1
        t.save()
        r['message'] = '删除成功'
    return jsonify(r)
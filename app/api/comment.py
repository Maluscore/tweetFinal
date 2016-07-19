from . import main
from ..models import Tweet
from flask import request
from flask import jsonify




# 添加评论
@main.route('/comment/open', methods=['POST'])
def comment_add():
    form = request.get_json()
    print('AJAX传递成功，form是：', form)
    tweet_id = form.get('id')
    tweet = Tweet.query.filter_by(id=tweet_id).first()
    comments = tweet.comments
    print('comments是：', comments)
    r = dict(
        message='展开成功!',
        success=True,
        data=comments,
    )
    return jsonify(r)

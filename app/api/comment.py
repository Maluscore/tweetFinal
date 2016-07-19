from . import main
from ..models import Tweet
from ..models import Comment
from . import current_user
from flask import request
from flask import jsonify




# 展开评论
@main.route('/comment/open', methods=['POST'])
def comment_open():
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


# 处理评论
@main.route('/tweet/comment', methods=['POST'])
def comment_add():
    u = current_user()
    form = request.get_json()
    print('AJAX传递成功，form是：', form)
    comment = Comment(form)
    comment.tweet_id = form['id']
    comment.sender_name = u.username
    print('comment is :', comment)
    r = dict(
        success=True,
        message='评论成功！',
        data = comment,
    )
    if len(form['content']) < 1:
        r['success'] = False
        r['message'] = '评论失败'
    return jsonify(r)

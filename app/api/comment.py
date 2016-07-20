from . import main
from . import current_user
from ..models import Tweet
from ..models import Comment
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
    all_c = []
    for c in comments:
        all_c.append(c.json())
    r = dict(
        message='展开成功!',
        success=True,
        data=all_c,
    )
    return jsonify(r)


# 关闭评论
@main.route('/comment/close', methods=['POST'])
def comment_close():
    form = request.get_json()
    print('关闭评论，form是：', form)
    tweet_id = form.get('id')
    tweet = Tweet.query.filter_by(id=tweet_id).first()
    data = {
        'com_count': tweet.com_count,
    }
    r = dict(
        message='展开成功!',
        success=True,
        data=data,
    )
    return jsonify(r)


# 处理评论
@main.route('/tweet/comment', methods=['POST'])
def comment_add():
    u = current_user()
    form = request.get_json()
    print('AJAX传递成功，form是：', form)
    c = Comment(form)
    c.tweet_id = form['id']
    c.sender_name = u.username
    c.save()
    print('comment is :', c)
    r = dict(
        success=True,
        message='评论成功！',
        data=c.json(),
    )
    t = Tweet.query.filter_by(id=form['id']).first()
    t.com_count += 1
    t.save()
    if len(form['content']) < 1:
        r['success'] = False
        r['message'] = '评论失败'
    # 不能直接jsonify，因为这个实例
    return jsonify(r)

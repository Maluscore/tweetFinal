from . import main
from flask import request




# 添加评论
@main.route('/comment/add', methods=['POST'])
def comment_add():
    form = request.get_json()

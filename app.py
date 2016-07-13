# from flask import Flask
# from flask import redirect
# from flask import url_for
#
# from api.login import api_login
# from api.login_view import api_login_view
# from api.register import api_register
# from api.timeline import api_timeline
# from api.tweet_add import api_tweet_add
# from app.api.time_filter import formatted_time
#
# app = Flask(__name__)
# app.secret_key = 'random string'
#
# app.jinja_env.filters['formatted_time'] = formatted_time
#
# # 通过 session 来获取当前登录的用户
# # def current_user():
# #     # print('session, debug', session.permanent)
# #     username = session.get('username', '')
# #     u = User.query.filter_by(username=username).first()
# #     return u
#
#
# @app.route('/')
# def index():
#     view = 'api_login_view.login_view'
#     return redirect(url_for(view))
#
# app.register_blueprint(api_login_view)
# # # 显示登录界面的函数  GET
# # @app.route('/login')
# # def login_view():
# #     return render_template('login.html')
#
# app.register_blueprint(api_login)
# # 处理登录请求  POST
# # @app.route('/login', methods=['POST'])
# # def login():
# #     # u = User(request.form)
# #     form = request.get_json()
# #     username = form.get('username', '')
# #     user = User.query.filter_by(username=username).first()
# #     # r = {
# #     #     'success': False,
# #     #     'message': '登录失败',
# #     #     'next': '',
# #     # }
# #     r = ResponseData()
# #     if user is not None and user.validate_auth(form):
# #         r.success = True
# #         r.message = '登录成功'
# #         r.next = url_for('timeline_view', user_id=user.id)
# #         session.permanent = True
# #         session['username'] = username
# #     else:
# #         r.message = '登录失败'
# #     r = r.jsonstr()
# #     # print("r is ,", r)
# #     return jsonify(r)
#
# app.register_blueprint(api_register)
# # 处理注册的请求  POST
# # @app.route('/register', methods=['POST'])
# # def register():
# #     form = request.get_json()
# #     # print('debug, ', form)
# #     u = User(form)
# #     # print('debug, ', u)
# #     # r = {
# #     # }
# #     r = ResponseData()
# #     status, msgs = u.valid()
# #     if status:
# #         u.save()
# #         r.success = True
# #         r.next = url_for('timeline_view', user_id=u.id)
# #         # 下面这句可以在关闭浏览器后保持用户登录
# #         session.permanent = True
# #         session['username'] = u.username
# #     else:
# #         r.message = '\n'.join(msgs)
# #     r = r.jsonstr()
# #     print("r is ,", r)
# #     return jsonify(r)
#
# app.register_blueprint(api_tweet_add)
# # @app.route('/post/tweet/add', methods=['POST'])
# # def tweet_add():
# #     form = request.get_json()
# #     tweet = Tweet(form)
# #     u = current_user()
# #     tweet.user_id = u.id
# #     r = ResponseData()
# #     content = tweet.content
# #     if content is not None:
# #         tweet.save()
# #         r.content = content
# #         r.success = True
# #     else:
# #         r.message = '请输入有效内容'
# #     r = r.jsonstr()
# #     return jsonify(r)
#
# app.register_blueprint(api_timeline)
# # @app.route('/timeline/<user_id>')
# # def timeline_view(user_id):
# #     return render_template('timeline.html', user_id=user_id)
#
#
# if __name__ == '__main__':
#     config = {
#         'debug': True,
#     }
#     app.run(**config)

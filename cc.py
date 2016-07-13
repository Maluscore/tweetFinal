# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# # from sqlalchemy import sql
#
#
# import time
# import shutil
#
# # 数据库的路径
# db_path = './db.sqlite'
# # 获取 app 的实例
# app = Flask(__name__)
# # app = app.app
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.secret_key = 'random string'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path)
#
# db = SQLAlchemy(app)
#
#
#
#
#
#
#
#
# def backup_db():
#     backup_path = '{}.{}'.format(time.time(), db_path)
#     shutil.copyfile(db_path, backup_path)
#
#
# # 定义了数据库，如何创建数据库呢？
# # 调用 db.create_all()
# # 如果数据库文件已经存在了，则啥也不做
# # 所以说我们先 drop_all 删除所有表
# # 再重新 create_all 创建所有表
# def rebuild_db():
#     # backup_db()
#     db.drop_all()
#     db.create_all()
#     print('rebuild database')
#
#
# # 第一次运行工程的时候没有数据库
# # 所以我们运行 models.py 创建一个新的数据库文件
# if __name__ == '__main__':
#     rebuild_db()

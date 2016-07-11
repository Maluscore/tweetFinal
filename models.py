from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import sql


import time
import shutil

# 数据库的路径
db_path = './db.sqlite'
# 获取 app 的实例
app = Flask(__name__)
# app = app.app
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = 'random string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path)

db = SQLAlchemy(app)


class ReprMixin(object):
    def __repr__(self):
        class_name = self.__class__.__name__
        return u'<{}: {}>'.format(class_name, self.id)


class User(db.Model, ReprMixin):
    # 类的属性就是数据库表的字段
    # 这些都是内置的 __tablename__ 是表名
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    created_time = db.Column(db.Integer, default=0)
    tweets = db.relationship('Tweet', backref='user')

    # 这是引用别的表的数据的属性，表明了它关联的东西
    # tweets = db.relationship('Tweet', backref='user')

    def __init__(self, form):
        super(User, self).__init__()
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        self.created_time = int(time.time())

    def json(self):
        # 加上这个就可以了
        self.id
        _dict = self.__dict__.copy()
        d = {k: v for k, v in _dict.items() if k not in self.blacklist()}
        # d['topics'] = [t.json() for t in self.topics]
        print('debug d, ', d)
        return d

    def blacklist(self):
        b = [
            'password',
            'created_time',
            'id',
            '_sa_instance_state',
        ]
        return b


    def validate_auth(self, form):
        username = form.get('username', '')
        password = form.get('password', '')
        username_equals = self.username == username
        password_equals = self.password == password
        return username_equals and password_equals

    def update(self, form):
        print('user.update, ', form)
        self.password = form.get('password', self.password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # 验证注册用户的合法性的
    def valid(self):
        valid_username = User.query.filter_by(username=self.username).first() is None
        valid_username_len = len(self.username) >= 3
        valid_password_len = len(self.password) >= 3
        msgs = []
        if not valid_username:
            message = '用户名已经存在'
            msgs.append(message)
        elif not valid_username_len:
            message = '用户名长度必须大于等于 3'
            msgs.append(message)
        elif not valid_password_len:
            message = '密码长度必须大于等于 3'
            msgs.append(message)
        status = valid_username and valid_username_len and valid_password_len
        return status, msgs


class Tweet(db.Model, ReprMixin):
    __tablename__ = 'tweets'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    created_time = db.Column(db.Integer, default=0)
    com_count = db.Column(db.Integer, default=0)
    # 这是一个外键
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, form):
        self.content = form.get('content', '')
        self.created_time = int(time.time())

    def json(self):
        self.id  # 加上这个就可以了
        _dict = self.__dict__.copy()
        d = {k: v for k, v in _dict.items() if k not in self.blacklist()}
        return d

    def blacklist(self):
        b = [
            '_sa_instance_state',
        ]
        return b

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, form):
        self.content = form.get('content', '')
        self.created_time = int(time.time())
        return True


class ResponseData(object):
    def __init__(self):
        self.success = False
        self.message = ''

    def jsonstr(self):
        r = self.__dict__
        return r


def backup_db():
    backup_path = '{}.{}'.format(time.time(), db_path)
    shutil.copyfile(db_path, backup_path)


# 定义了数据库，如何创建数据库呢？
# 调用 db.create_all()
# 如果数据库文件已经存在了，则啥也不做
# 所以说我们先 drop_all 删除所有表
# 再重新 create_all 创建所有表
def rebuild_db():
    # backup_db()
    db.drop_all()
    db.create_all()
    print('rebuild database')


# 第一次运行工程的时候没有数据库
# 所以我们运行 models.py 创建一个新的数据库文件
if __name__ == '__main__':
    rebuild_db()

from . import db
from . import ReprMixin

import time


class Like(db.Model, ReprMixin):
    __tablename__ = 'likes'
    id = db.Column(db.Integer, primary_key=True)
    created_time = db.Column(db.Integer, default=0)
    tweet_id = db.Column(db.Integer, db.ForeignKey('tweets.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    users = db.relationship('User')

    def __init__(self):
        self.created_time = int(time.time())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
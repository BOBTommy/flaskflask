# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String, unique=True)
    user_password = db.Column(db.String)

    def __repr__(self):
        return u"%r" % self.user_email


@app.route('/')
def index():
    c_set = [u"서울", u"판교", u"파리", u"도쿄"]
    return render_template('index.html',
                           c_set=c_set)

@app.route('/login')
def login():
    c_set = [u"서울", u"판교", u"파리", u"도쿄"]
    return render_template('login.html',
                           c_set=c_set)

if __name__ == '__main__':
    app.run(debug=True)

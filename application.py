# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
#from flask.ext.sqlalchemy import SQLAlchemy
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

@app.route('/')
def index():
    c_set = ["서울","판교","파리","도쿄"]
    return render_template('index.html',
                           c_set = c_set)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
from flask_moment import Moment

#The upper part of the code
app = Flask(__name__)
moment = Moment(app)

from datetime import datetime

@app.route('/')
@app.route('/hh')
def home_page():
    return render_template('home.html', current_time = datetime.utcnow())

@app.route('/user/<name>')
def user(name):
         return render_template("helloUser.html", name=name)

#Error finding the value
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#internal server eroor 
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500







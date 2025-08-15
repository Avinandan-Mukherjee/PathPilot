from flask import Flask, render_template, flash, redirect
from forms import RegisterForm, LoginForm

from dotenv import load_dotenv
import os
load_dotenv()
flask_key = os.getenv('FLASK_KEY')


app = Flask(__name__)
app.config['SECRET_KEY'] = flask_key

@app.route("/")
def chat():
    return


@app.route("/register", methods = ['GET', 'POST'])
def register():
    form  = RegisterForm()
    if form.validate_on_submit():
        flash('Successfully Created Account')
        return redirect(chat)
    return render_template('register.html', form = form)


@app.route("/login")
def login():
    form  = LoginForm()
    return render_template('login.html', form = form)


@app.route("/resume")
def resume():
    return

@app.route("/interview")
def interview():
    return


app.run(debug=True)
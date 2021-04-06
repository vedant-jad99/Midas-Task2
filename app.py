#!/usr/bin/env python3

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm1, LoginForm2

app = Flask(__name__)
app.config["SECRET_KEY"] = 'ff127ef745c8859dd6509413570a5bd3'

@app.route('/')
@app.route('/home')
def home():
    return render_template("main.html")

@app.route("/registration", methods=["GET", "POST"])
def registration():
    form = RegistrationForm()
    if not form.validate_on_submit():
        print("Not-valid")
    else:
        flash('Account created for {}'.format(form.username.data), 'success') 
        return redirect(url_for('login1'))
    return render_template("registration.html", title="Sign Up", form=form)

@app.route("/login-username", methods=["GET", "POST"])
def login1():
    form = LoginForm1()
    if not form.validate_on_submit():
        print("Not valid")
    return render_template("username-login.html", title="Login", form=form)

@app.route("/login-email", methods=["GET", "POST"])
def login2():
    form = LoginForm2()
    if not form.validate_on_submit():
        print("Not valid")
    return render_template("email-login.html", title="Login", form=form)


if __name__ == '__main__':
    app.run(debug=True)
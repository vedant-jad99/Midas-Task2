from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import RegistrationForm, LoginForm1, LoginForm2
from app.models import User

@app.route('/')
@app.route('/home')
def home():
    return render_template("main.html")

@app.route("/registration", methods=["GET", "POST"])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        app.logger.info("All information valid")
        hash_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, username=form.username.data\
            , email=form.email.data, password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created for {}'.format(form.username.data), 'success') 
        return redirect(url_for('login1'))
    else:
        app.logger.warning(str([error for error in form.errors]) + " form elements have error")
    return render_template("registration.html", title="Sign Up", form=form)

@app.route("/login-username", methods=["GET", "POST"])
def login1():
    form = LoginForm1()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template("username-login.html", title="Login", form=form)

@app.route("/login-email", methods=["GET", "POST"])
def login2():
    form = LoginForm2()
    if form.validate_on_submit():
        app.logger.info("All information valid")
        return redirect(url_for("home"))
    return render_template("email-login.html", title="Login", form=form)

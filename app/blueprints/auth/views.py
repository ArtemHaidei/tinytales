from flask import render_template, redirect, url_for, flash
from .forms import SignUpForm, SignInForm
from werkzeug.security import generate_password_hash, check_password_hash
from ..users import User
from app import db


def sing_in():
    form = SignInForm()

    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()

        if not user:
            flash("User with this email doesn't exist!", category='email_error')


        if user.check_password(form.password.data):
            return "<h1>You sign in successfully!</h1>"
        else:
            flash("Wrong password!", category='password_error')

    return render_template(
        'auth/sign_in.html',
        title='Sign In',
        form=form,
    )


def sign_up():
    form = SignUpForm()

    if form.validate_on_submit():
        email = email=form.email.data
        user = User.query.filter_by(email=form.email.data).first()

        if user:
            return f"<h1>User with {email} already exists!</h1>"

        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=email,
            password=form.password.data,
        )
        db.session.add(user)
        db.session.commit()

        return f"<h1>Congratulations, your account with {email} and {form.password.data} has been created successfully!</h1>"

    return render_template(
        'auth/sign_up.html',
        title='Sign Up',
        form=form,
    )

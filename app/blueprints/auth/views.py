from flask import render_template, redirect, url_for, flash
from .forms import SignUpForm, SignInForm
from werkzeug.security import generate_password_hash, check_password_hash
from ..users import User
from app import db
from flask_login import login_user, logout_user, login_required, current_user
from app import login_manager


@login_manager.user_loader
def load_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    return user if user else None


#TODO: url_has_allowed_host_and_scheme
def sing_in():
    form = SignInForm()

    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()

        if not user:
            flash("User with this email doesn't exist!", category='email_error')

        if user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('posts.blog'))
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
            flash("User with this email already exists!", category='email_error')

        user = User.query.filter_by(email=form.nickname.data).first()
        if user:
            flash("User with this nickname already exists!", category='nickname_error')

        user = User(
            full_name=form.full_name.data,
            nickname=form.nickname.data,
            email=email,
            password=form.password.data,
        )
        db.session.add(user)
        db.session.commit()

        return (
            f"<h1>Congratulations, your account with {email} has been created successfully!</h1>"
            f"<a href='{url_for('auth.sign-in')}'>Sign in</a>"
        )

    return render_template(
        'auth/sign_up.html',
        title='Sign Up',
        form=form,
    )


@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))

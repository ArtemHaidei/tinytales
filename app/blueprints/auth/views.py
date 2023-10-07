from flask import render_template, redirect, url_for
from .forms import SignUpForm, SignInForm


def sing_in():
    name = None
    form = SignInForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print(email, password)
        return "<h1>Sign In Success</h1>"

    return render_template(
        'auth/sign_in.html',
        title='Sign In',
        form=form,
    )


def sign_up():
    name = None
    form = SignUpForm()

    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data
        print(first_name, last_name, email, password)
        return "<h1>Sign Up Success</h1>"

    return render_template(
        'auth/sign_up.html',
        title='Sign Up',
        form=form,
    )

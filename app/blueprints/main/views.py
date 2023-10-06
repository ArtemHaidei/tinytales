from flask import render_template


def home():
    return render_template('main/home.html', title='Home')


def about():
    return render_template('main/about.html', title='About')


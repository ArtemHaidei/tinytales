from flask import render_template


def page_not_found(e):
    return render_template('main/404.html', title='Page not found!'), 404

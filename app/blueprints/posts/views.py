from flask import render_template
from .forms import PostForm


def posts():
    return render_template('posts/posts.html', title='Posts')


def blog():
    return render_template('posts/blog.html', title='Blog')


def post_create():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        status = form.status.data
        print(title, content, status)
        return "<h1>Post Create Success</h1>"
    return render_template('posts/post_create.html', title='Create Post', form=form)
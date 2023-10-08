from flask import render_template, flash, url_for
from .forms import PostForm


def posts():
    return render_template('posts/posts.html', title='Posts')


def blog():
    return render_template('posts/blog.html', title='Blog')


def post_create():
    form = PostForm()
    post_created = False
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        status = form.status.data
        post_created = True
        flash('Post Create Success! You can see it in the blog page.')

    return render_template('posts/post_create.html', title='Create Post', form=form, post_created=post_created)

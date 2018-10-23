from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import BlogForm,SubscriberForm,CommentForm
from ..import db,photos
from ..models import User,Blog,Role,Subscriber,Comment
from flask_login import login_required,current_user
import markdown2
from ..email import mail_message

#Views
@main.route("/",methods=['GET','POST'])
def index():
    """
    View root page function that returns the index page and its data
    """
    blogs = Blog.query.all()
    form = SubscriberForm()
    if form.validate_on_submit():
        email = form.email.data

        new_subscriber=Subscriber(email=email)
        new_subscriber.save_subscriber()

        mail_message("Subscription Received","email/subscribtion",new_subscriber.email,subscriber=new_subscriber)

    title = "Welcome to My Blog"
    return render_template('index.html',title=title,blogs=blogs,subscriber_form=form)

@main.route("/new_blog",methods=['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        blog = form.blog.data
        category = form.category.data
        like=0
        new_blog=Blog(title=title,blog=blog,category=category,like=like)

        new_blog.save_blog()

        subscribers=Subscriber.query.all()

        for subscriber in subscribers:
            mail_message("New Blog Blog","email/new_blog",subscriber.email,blog=new_blog)

        return redirect(url_for('main.index'))

    title="Make a story"
    return render_template('new_blog.html',title=title,blog_form=form)

@main.route("/blog/<int:id>",methods=['GET','POST'])
def blog(id):
    blog=Blog.query.get_or_404(id)
    comment = Comment.query.all()
    form=CommentForm()

    if request.args.get("like"):
        blog.like = blog.like+1

        db.session.add(blog)
        db.session.commit()

        return redirect("/blog/{blog_id}".format(blog_id=blog.id))

    if form.validate_on_submit():
        comment=form.comment.data
        new_comment = Comment(id=id,comment=comment,user_id=current_user.id,blog_id=blog.id)

        new_comment.save_comment()

        return redirect("/blog/{blog_id}".format(blog_id=blog.id))

    return render_template('blog.html',blog=blog,comments=comment,comment_form=form)
@main.route("/anime",methods=['GET','POST'])
def anime():
    """
    View root page function that returns the index page and its data
    """
    blogs = Blog.query.filter_by(category="Anime").all()
    form = SubscriberForm()
    if form.validate_on_submit():
        email = form.email.data

        new_subscriber=Subscriber(email=email)
        new_subscriber.save_subscriber()

        mail_message("Subscription Received","email/subscribtion",new_subscriber.email,subscriber=new_subscriber)

    title = "Welcome to My Blog"
    return render_template('anime.html',title=title,blogs=blogs,subscriber_form=form)
@main.route("/gaming",methods=['GET','POST'])
def gaming():
    """
    View root page function that returns the index page and its data
    """
    blogs = Blog.query.filter_by(category="Gaming").all()
    form = SubscriberForm()
    if form.validate_on_submit():
        email = form.email.data

        new_subscriber=Subscriber(email=email)
        new_subscriber.save_subscriber()

        mail_message("Subscription Received","email/subscribtion",new_subscriber.email,subscriber=new_subscriber)

    title = "Welcome to My Blog"
    return render_template('gaming.html',title=title,blogs=blogs,subscriber_form=form)

@main.route("/tech",methods=['GET','POST'])
def tech():
    """
    View root page function that returns the index page and its data
    """
    blogs = Blogs.query.filter_by(category="Tech").all()
    form = SubscriberForm()
    if form.validate_on_submit():
        email = form.email.data

        new_subscriber=Subscriber(email=email)
        new_subscriber.save_subscriber()

        mail_message("Subscription Received","email/subscribtion",new_subscriber.email,subscriber=new_subscriber)

    title = "Welcome to My Blog"
    return render_template('tech.html',title=title,blogs=blogs,subscriber_form=form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

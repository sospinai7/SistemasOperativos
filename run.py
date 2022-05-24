from flask import Flask, render_template
app = Flask(__name__)

posts = []

@app.route("/")
def index():
    return render_template("index.html", num_posts=len(posts))

@app.route('/open')
def app3_open():
    return render_template("app3.html")

@app.route('/close')
def app3_close():
    return render_template("app3.html")


@app.route("/p/<string:slug>/")
def show_post(slug):
    return render_template("post_view.html", slug_title=slug)


@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>/")
def post_form(post_id=None):
    return render_template("admin/post_form.html", post_id=post_id)
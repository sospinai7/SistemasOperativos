from flask import Flask, render_template
import sys

from kernel import kernel

app = Flask(__name__)
app.register_blueprint(kernel, url_prefix='/kernel')

posts = []

@app.route("/")
def index():
    print("inicio el programa")
    return render_template("index.html", num_posts=len(posts))
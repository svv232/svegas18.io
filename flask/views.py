from flask import Blueprint
from flask import render_template
from jinja2 import Template

views = Blueprint('views', __name__)

@views.route("/")
def index():
    return render_template("index.html")

@views.route("/about-me")
def about():
    return render_template("about-me.html")

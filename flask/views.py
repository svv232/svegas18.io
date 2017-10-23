from flask import Blueprint
from flask import render_template

views = Blueprint('views', __name__)

@views.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@views.route("/about-me", methods=['GET'])
def about():
    return render_template("about-me.html")

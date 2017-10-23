from flask import Flask
from flask import render_template
import os

app = Flask(__name__, static_url_path=str(os.path.dirname(__file__)))

#app.config["APPLICATION__ROOT"] = "/mnt/c/Users/Sai Vegasena/Downloads/summer/flask"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about-me")
def about():
    return render_template("about-me.html")

if __name__ == "__main__":
    app.run()

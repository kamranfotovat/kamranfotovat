from flask import Flask, flash, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from cs50 import SQL
from tools import login_required
from tempfile import mkdtemp
from flask_session import Session



app = Flask(__name__)



app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///barca.db")

@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST","GET"])
def login():

    if request.method == "post":

        name = request.form.get("username")
        password = request.form.get("password")


        if not name:
            pass

        if not password:
            pass

        return redirect("index.html")

    else:
        return render_template("login.html")

@app.route("/register", methods=["POST","GET"])
def register():
    if request.method == "post":

        


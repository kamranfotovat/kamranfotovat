from flask import Flask, render_template, request, redirect
from score import increase, report_score


app = Flask(__name__)


@app.route("/")
def questions():

    return render_template("question.html")








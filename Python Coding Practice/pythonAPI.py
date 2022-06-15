from webbrowser import get
import flask
from flask import Flask, render_template, request
import math
from time import sleep

# dollar_conversion_multiple = 78
# yen_conversion_multiple = 1.72
# ukdollar_conversion_multiple = 0.011
# r=1

app = Flask(__name__)


@app.route("/")
def resume():
    return render_template('index.html')

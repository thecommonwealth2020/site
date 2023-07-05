from flask import Flask
from flask import render_template
import os

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def home_page():
    return render_template('index.html')
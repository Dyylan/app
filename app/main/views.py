from flask import render_template, session, redirect, url_for, current_app
from . import main

@main.route('/')
def index():
    return render_template('index.html')
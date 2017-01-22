from app import app
from flask import render_template, request


@app.route('/')
def homepage():
    name = request.args.get('name')
    number = request.args.get('number')
    if not name:
        name = '<unknown>'
    return render_template('homepage.html', name=name, number=number)
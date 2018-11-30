from flask import request, render_template, jsonify
from app import app
# from app import db
# from app.models.main import User
from app.utils.main import helloWorld


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello-world')
def hello():
    response = helloWorld()

    return jsonify({'response': response})

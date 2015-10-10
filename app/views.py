from app import app
from flask import render_template

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about/')
def professional():
	return render_template('about.html')

@app.route('/schedule/')
def creative():
	return render_template('schedule.html')

@app.route('/news/')
def fun():
	return render_template('news.html')

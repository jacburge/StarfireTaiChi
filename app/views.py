from app import app
from flask import render_template

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about/')
def about():
	return render_template('about.html')

@app.route('/schedule/')
def schedule():
	return render_template('schedule.html')

@app.route('/news/')
def news():
	return render_template('news.html')

@app.route('/retreat/')
def retreat():
	return render_template('retreat.html')
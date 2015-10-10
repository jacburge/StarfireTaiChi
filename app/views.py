from app import app
from flask import render_template

@app.route('/')
def index():
	return render_template('index.html')

@app.route('../templates/about/')
def professional():
	return render_template('about.html')

@app.route('../templates/schedule/')
def creative():
	return render_template('schedule.html')

@app.route('../templates/news/')
def fun():
	return render_template('news.html')

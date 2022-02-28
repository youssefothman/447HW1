from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add')
def add():
    return render_template("add.html")

@app.route('/update')
def update():
    return render_template("update.html")

@app.route('/delete')
def delete():
    return render_template("delete.html")
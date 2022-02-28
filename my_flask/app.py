from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///imports.db'

db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    points = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Name %r>' % self.id

@app.route('/')
def index():
    people = Person.query.order_by(Person.id)
    return render_template("index.html", people=people)

@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == "POST":
        person_name = request.form['name']
        person_id = request.form['id']
        person_points = request.form['points']
        new_person = Person(id=person_id, name=person_name, points=person_points)

        try:
            db.session.add(new_person)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an error adding that person."

    else:
        people = Person.query.order_by(Person.id)
        return render_template("add.html", people=people)

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    id_to_update = Person.query.get_or_404(id)
    if request.method == "POST":
        id_to_update.points = request.form['points']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "Ther was an error updating that person's points."
    else:
        return render_template("update.html", id_to_update=id_to_update)

@app.route('/delete')
def delete():
    return render_template("delete.html")
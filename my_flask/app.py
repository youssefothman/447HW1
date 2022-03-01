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
    return render_template("index.html", people=people, id_to_search=0)

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
            return "There was an error updating that person's points."
    else:
        return render_template("update.html", id_to_update=id_to_update)

@app.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete(id):
    id_to_delete = Person.query.get_or_404(id)
    if request.method == "POST":
        try:
            db.session.delete(id_to_delete)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an error deleting that person."
    else:
        return render_template("delete.html", id_to_delete=id_to_delete)


@app.route('/search/<int:id>', methods=['POST', 'GET'])
def search(id):
    id_to_search = Person.query.get_or_404(id)
    if request.method == "POST":
        try:
            db.session.commit()
            return render_template('search.html',id_to_search=id_to_search)
        except:
            return "That ID does not match anyone."
    else:
        return render_template("search.html", id_to_search=id_to_search)

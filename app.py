from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Insurance_list(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(50))


    def __init__(self, name, email, phone):

        self.name = name
        self.email = email
        self.phone = phone

@app.route('/')
def evidence():
    all_data = Insurance_list.query.all()

    return render_template("pojisteni.html", users = all_data)

@app.route('/add', methods = ['POST'])
def insert():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']


        my_data = Insurance_list(name, email, phone)
        db.session.add(my_data)
        db.session.commit()

        return redirect(url_for('evidence'))

@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Insurance_list.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    return redirect(url_for('evidence'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
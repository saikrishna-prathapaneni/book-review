import csv
import os
from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:Saikri@23@localhost/book_review")
db = scoped_session(sessionmaker(bind=engine))


app = Flask(__name__)

@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("main_ind.html", flights=flights)



@app.route("/book",methods=['POST'])
def book():

    name=request.form.get('name')
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number.")
    if db.execute('SELECT * FROM flights WHERE id=:id',{'id':flight_id}).rowcount==0:
        return render_template('error.html')

    db.execute('INSERT INTO passengers (name,flight_id) VALUES (:na,:fi)',{'na':name,'fi':flight_id})
    db.commit()
    return render_template('success.html',msg="hell ya!")

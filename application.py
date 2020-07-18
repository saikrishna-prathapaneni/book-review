import csv
import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:Saikri@23@localhost/book_review")
db = scoped_session(sessionmaker(bind=engine))


dbs=SQLAlchemy()

class passengers():
    pass


class books():
    pass




app = Flask(__name__)

@app.route("/")
def home():
    return render_template("main_ind.html")

@app.route("/login")
def login():
     email=request.form.get('login id')
     password=request.form.get('password')
     if db.execute('SELECT * FROM users WHERE email=:id AND pass=:password',{'id':email,'password':password}).rowcount==0:
         return render_template('error.html')
        
        
     db.execute('SELECT * FROM users WHERE email=:id AND pass=:password',{'id':email,'password':password})
     return render_template('user.html',msg=email)
@app.route("/create")
def create():
     email=request.form.get('login id')
     password=request.form.get('confirm password')

     db.execute('INSERT INTO users (email,pass) VALUES (:na,:fi)',{'na':email,'fi':password})
     db.commit()
     return render_template('success.html',msg="hell ya!")

     



#@app.route("/hello")
#def index():
#    return render_template("user.html")
#@app.route("/create",methods=['POST'])
#def create():
#   email=request.form.get('login id')
#    password=request.form.get('password')

#    try:
#        flight_id = int(request.form.get("flight_id"))
 #   except ValueError:
 #       return render_template("error.html", message="Invalid flight number.")
#    if db.execute('SELECT * FROM users WHERE id=:id',{'id':flight_id}).rowcount==0:
#        return render_template('error.html')

#   db.execute('INSERT INTO passengers (name,flight_id) VALUES (:na,:fi)',{'na':name,'fi':flight_id})
#    db.commit()
#    return render_template('success.html',msg="hell ya!")

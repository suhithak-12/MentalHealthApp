import os
from dotenv import load_dotenv, dotenv_values
from flask import Flask, request, jsonify
import mysql.connector

""" Notes: 
    RELEVANT INSTALLS: 
    need: 
    pip install flask and 
    pip install python-dotenv
    
    using a .env file to store DB credentials. In your .env file, have:
    DB_ENDPOINT = put the db endpoint/host 
    DB_USER = put the db username
    DB_PASSWORD = put the db password

    RUNNING THE FLASK API:
    flask --app api --debug run 
    THIS NEEDS TO BE STARTED FIRST IN A SEPARATE TERMINAL,
    then run the kivy files in another terminal. Else kivy/flask 
    will block each other - so we need separate processes
"""

app = Flask(__name__)

def connhelper(): #helper function to establish connection
    load_dotenv() #grabbing values from .env file
    dbconn = mysql.connector.connect(
        host = os.getenv("DB_ENDPOINT"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME", "project-schema") #might hide this in the .env later
    )
    return dbconn

@app.route("/")
def test_point():
    return "making sure this works :)" #you will see this text if you navigate to http://127.0.0.1:5000 (assuming flask is on port 5000)

@app.route("/login", methods=["POST"]) #creating endpoint, only for post requests for login safety
def login():
    usernameData = request.form.get('username') #gets the data, data sent in request treated as form data
    password = request.form.get('password')
    #establish db connection
    dbconn = connhelper()
    mycursor = dbconn.cursor()
    sql = "SELECT * FROM user WHERE username = %s AND password=%s" #getting data from user table in db
    adr = (usernameData, password)
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchall()
    return jsonify(myresult)  #send data back in JSON object/ if we dont the record will be a string

@app.route("/create", methods=["POST"])
def accountcreate():
    usernamedata = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    dbconn = connhelper()
    sql = "INSERT INTO user (username, password, email) VALUES (%s, %s, %s)"
    vals = (usernamedata, password, email)
    mycursor = dbconn.cursor()
    try:
        mycursor.execute(sql, vals)
        dbconn.commit()
    except: 
        return "Did not Insert"
    return "Creation Successful"

if __name__=='__main__':
    app.run(debug=True)


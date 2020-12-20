from flask import Flask, flash, request, url_for, redirect, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime
from utils.db import insert
from utils.validate import logval
import urllib.request,time
import json

app = Flask(__name__)
app.secret_key = "Random"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/student_login",methods=["GET","POST"])
def student_login():
    if request.method == "POST":
        req = request.form
        status = logval(req)
        print(status)
        if(status != "Success"):
            return redirect("/student_login")
        else:
            return redirect("/profile")
    return render_template("student_login.html")

@app.route("/teacher_login",methods=["GET","POST"])
def teacher_login():
    if request.method == "POST":
        req = request.form
        status = logval(req)
        print(status)
        if(status != "Success"):
            return redirect("/teacher_login")
        else:
            return redirect("/profile")
    return render_template("teacher_login.html")

@app.route("/adminlogin",methods=["GET","POST"])
def adminlogin():
    if request.method == "POST":
        req = request.form
        if req["email"]=="ADMIN" and req["password"]=="ADMIN":
            return redirect("/admin")
        else:
            return redirect("/adminlogin")
    return render_template("adminlogin.html")

@app.route("/student_signup",methods=["GET","POST"])
def student_signup():
    status = None
    if request.method == "POST":
        req = request.form
        status = insert(req)
        print(status)
        if(status != "Success"):
            return redirect("/student_signup")
        else:
            return redirect("/student_login")
    return render_template("student_signup.html",error = status)

@app.route("/teacher_signup",methods=["GET","POST"])
def teacher_signup():
    status = None
    if request.method == "POST":
        req = request.form
        status = insert(req)
        print(status)
        if(status != "Success"):
            return redirect("/teacher_signup")
        else:
            return redirect("/teacher_login")
    return render_template("teacher_signup.html",error = status)

@app.route("/admin")
def admin():
    return render_template("adminprofile.html")    

@app.route("/addbook")
def addbook():
    return render_template("addbook.html")

@app.route("/adduser")
def adduser():
    return render_template("adduser.html")

@app.route("/removebook")
def removebook():
    return render_template("removebook.html")

@app.route("/removeuser")
def removeuser():
    return render_template("removeuser.html")

@app.route("/viewbooks")
def viewbooks():
    return render_template("viewbooks.html")

@app.route("/viewusers")
def viewusers():
    return render_template("viewusers.html")

@app.route("/bookhistory")
def bookhistory():
    return render_template("bookhistory.html")

@app.route("/userhistory")
def userhistory():
    return render_template("userhistory.html")

@app.errorhandler(404)
def err_404(e):
    return render_template("err_404.html")

if __name__ == "__main__":
    app.run(debug=True,host="localhost",port=5000)
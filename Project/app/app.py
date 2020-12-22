from flask import Flask, flash, request, url_for, redirect, render_template, session, g
from flask_bootstrap import Bootstrap
from datetime import datetime
from utils.ins_val_db import stu_val, teach_val, S_logval, T_logval, book_val
from utils.del_val_db import stu_del, teach_del, book_del
from utils.display import stu_display, teach_display, book_display
from utils.writing import stu_write, teach_write, book_write
import urllib.request,time
import json
from tkinter import messagebox, Tk
  
top = Tk()  
top.geometry("100x100")  

app = Flask(__name__)
app.secret_key = "Random"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/student_login",methods=["GET","POST"])
def student_login():
    status = None
    if request.method == "POST":
        req = request.form
        status = S_logval(req)
        if(status != "Success"):
            return redirect("/student_login")
        else:
            return redirect("/studentprofile")
    return render_template("student_login.html")

@app.route("/teacher_login",methods=["GET","POST"])
def teacher_login():
    if request.method == "POST":
        req = request.form
        status = T_logval(req)
        if(status != "Success"):
            return redirect("/teacher_login")
        else:
            return redirect("/teacherprofile")
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
        status = stu_val(req)
        if(status != "Success"):
            return redirect("/student_signup")
        else:
            return redirect("/student_login")
    status1 = "Testing"
    return render_template("student_signup.html",data=status1)

@app.route("/teacher_signup",methods=["GET","POST"])
def teacher_signup():
    status = None
    if request.method == "POST":
        req = request.form
        status = teach_val(req)
        if(status != "Success"):
            return redirect("/teacher_signup")
        else:
            return redirect("/teacher_login")
    return render_template("teacher_signup.html",error = status)

@app.route("/admin")
def admin():
    return render_template("adminprofile.html") 

@app.route("/studentprofile")
def studentprofile():
    return render_template("studentprofile.html")

@app.route("/teacherprofile")
def teacherprofile():
    return render_template("teacherprofile.html")

@app.route("/admin/addbook",methods=["GET","POST"])
def addbook():
    status = None
    if request.method == "POST":
        req = request.form
        status = book_val(req)
        if(status != "Success"):
            return redirect("/addbook")
        else:
            return redirect("/admin")
    return render_template("addbook.html")

@app.route("/admin/addstudent",methods=["GET","POST"])
def addstudent():
    status = None
    if request.method == "POST":
        req = request.form
        status = stu_val(req)
        if(status != "Success"):
            return redirect("/addstudent")
        else:
            return redirect("/admin")
    return render_template("addstudent.html")

@app.route("/admin/removebook",methods=["GET","POST"])
def removebook():
    if request.method == "POST":
        req = request.form
        status = book_del(req)
        if(status == "Success"):
            return redirect("/admin")
        else:
            return redirect("/removebook")
    return render_template("removebook.html")

@app.route("/admin/removestudent",methods=["GET","POST"])
def removestudent():
    if request.method == "POST":
        req = request.form
        status = stu_del(req)
        if(status == "Success"):
            return redirect("/admin")
        else:
            return redirect("/removestudent")
    return render_template("removestudent.html")

@app.route("/admin/viewbooks",methods=["GET","POST"])
def viewbooks():
    data = list()
    data = book_display()
    if not data:
        msg = "No Books"
    else:
        msg = "The Books data has been written on the Book.csv file in the Downloads folder"
    flash(msg)
    book_write(data)
    return render_template("viewbooks.html")

@app.route("/admin/viewstudents",methods=["GET","POST"])
def viewstudents():
    data = list()
    data = stu_display()
    if not data:
        msg = "No Student Users"
    else:
        msg = "The Student Users data has been written on the Student_Users.csv file in the Downloads folder"
    flash(msg)
    stu_write(data)
    return render_template("viewstudents.html")

@app.route("/admin/bookhistory")
def bookhistory():
    return render_template("bookhistory.html")

@app.route("/admin/studenthistory")
def studenthistory():
    return render_template("studenthistory.html")

@app.route("/admin/addteacher",methods=["GET","POST"])
def addteacher():
    status = None
    if request.method == "POST":
        req = request.form
        status = teach_val(req)
        if(status != "Success"):
            return redirect("/addteacher")
        else:
            return redirect("/admin")
    return render_template("addteacher.html")

@app.route("/admin/removeteacher",methods=["GET","POST"])
def removeteacher():
    if request.method == "POST":
        req = request.form
        status = teach_del(req)
        if(status == "Success"):
            return redirect("/admin")
        else:
            return redirect("/removeteacher")
    return render_template("removeteacher.html")

@app.route("/admin/viewteachers",methods=["GET","POST"])
def viewteachers():
    data = list()
    data = teach_display()
    if not data:
        msg = "No Teacher Users"
    else:
        msg = "The Teacher Users data has been written on the Teacher_Users.csv file in the Downloads folder"
    flash(msg)
    teach_write(data)
    return render_template("viewteachers.html")

@app.route("/admin/teacherhistory")
def teacherhistory():
    return render_template("teacherhistory.html")

@app.route("/admin/studentupdate")
def studentupdate():
    return render_template("studentupdate.html")

@app.route("/admin/teacherupdate")
def teacherupdate():
    return render_template("teacherupdate.html")

@app.route("/admin/bookreturn")
def bookreturn():
    return render_template("bookreturn.html")

@app.route("/admin/studentborrow")
def studentborrow():
    return render_template("studentborrow.html")

@app.route("/admin/teacherborrow")
def teacherborrow():
    return render_template("teacherborrow.html")

@app.route("/admin/bookborrow")
def bookborrow():
    return render_template("bookborrow.html")

@app.errorhandler(404)
def err_404(e):
    return render_template("err_404.html")

@app.route("/login")
def logout():
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True,host="localhost",port=5000)
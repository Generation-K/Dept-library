from flask import Flask, flash, request, url_for, redirect, render_template, session, g
from flask_bootstrap import Bootstrap
from utils.ins_val_db import stu, teach, stu_val, teach_val, S_logval, T_logval, book_val, update
from utils.del_val_db import stu_del, teach_del, book_del, teach_del_acc, stu_del_acc
from utils.display import stu_display, teach_display, book_display, stu_history, teach_history, book_history
from utils.display import stu_det, teach_det, avail_books, p_teach_history, p_stu_history
from utils.writing import stu_write, teach_write, book_write, stu_history_csv, teach_history_csv, book_history_csv
from utils.borrow import admin_stu_borrow, admin_teach_borrow, returnbook
import urllib.request, time
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
        status = S_logval(req)
        if(status != "Success"):
            return redirect("/student_login")
        else:
            user = stu(req)
            session["user"] = user[0][0]
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
            user = teach(req)
            session["user"] = user[0][0]
            return redirect("/teacherprofile")
    return render_template("teacher_login.html")

@app.route("/adminlogin",methods=["GET","POST"])
def adminlogin():
    if request.method == "POST":
        req = request.form
        if req["email"]=="ADMIN" and req["password"]=="ADMIN":
            session["user"] = "ADMIN"
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
    return render_template("student_signup.html")

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
    return render_template("teacher_signup.html")

@app.route("/admin")
def admin():
    if "user" in session:
        user = session["user"]
    else:
        return redirect("/adminlogin")
    return render_template("adminprofile.html") 

@app.route("/studentprofile")
def studentprofile():
    if "user" in session:
        user = session["user"]
    else:
        return redirect("/student_login")
    return render_template("studentprofile.html")

@app.route("/teacherprofile")
def teacherprofile():
    if "user" in session:
        user = session["user"]
    else:
        return redirect("/teacher_login")
    return render_template("teacherprofile.html")

@app.route("/admin/addbook",methods=["GET","POST"])
def addbook():
    status = None
    if request.method == "POST":
        req = request.form
        status = book_val(req)
        if(status != "Success"):
            return redirect("/admin/addbook")
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
            return redirect("/admin/addstudent")
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
            return redirect("/admin/removebook")
    return render_template("removebook.html")

@app.route("/admin/removestudent",methods=["GET","POST"])
def removestudent():
    if request.method == "POST":
        req = request.form
        status = stu_del(req)
        if(status == "Success"):
            return redirect("/admin")
        else:
            return redirect("/admin/removestudent")
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
        stu_write(data)
        msg = "The Student Users data has been written on the Student_Users.csv file in the Downloads folder"
    flash(msg)
    return render_template("viewstudents.html")

@app.route("/admin/bookhistory")
def bookhistory():
    data = list()
    data = book_history()
    if not data:
        msg = "No Book History"
    else:
        msg = "The Books History data has been written on the Books_History.csv file in the Downloads folder"
        book_history_csv(data)
    flash(msg)
    return render_template("bookhistory.html")

@app.route("/admin/studenthistory",methods=["GET","POST"])
def studenthistory():
    data = list()
    data = stu_history()
    if not data:
        msg = "No Student History"
    else:
        msg = "The Student History data has been written on the Students_History.csv file in the Downloads folder"
        stu_history_csv(data)
    flash(msg)
    return render_template("studenthistory.html",data=data)

@app.route("/admin/addteacher",methods=["GET","POST"])
def addteacher():
    status = None
    if request.method == "POST":
        req = request.form
        status = teach_val(req)
        if(status != "Success"):
            return redirect("/admin/addteacher")
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
            return redirect("/admin/removeteacher")
    return render_template("removeteacher.html")

@app.route("/admin/viewteachers",methods=["GET","POST"])
def viewteachers():
    data = list()
    data = teach_display()
    if not data:
        msg = "No Teacher Users"
    else:
        msg = "The Teacher Users data has been written on the Teacher_Users.csv file in the Downloads folder"
        teach_write(data)
    flash(msg)
    return render_template("viewteachers.html")

@app.route("/admin/teacherhistory")
def teacherhistory():
    data = list()
    data = teach_history()
    if not data:
        msg = "No Teacher History"
    else:
        msg = "The Teacher History data has been written on the Teachers_History.csv file in the Downloads folder"
        teach_history_csv(data)
    flash(msg)
    return render_template("teacherhistory.html")

@app.route("/admin/bookreturn",methods=["GET","POST"])
def bookreturn():
    if request.method=="POST":
        req = request.form
        status = returnbook(req)
        if status == "Success":
            return redirect("/admin")
        else:
            return redirect("/admin/bookreturn")
    return render_template("bookreturn.html")

@app.route("/admin/studentborrow",methods=["GET","POST"])
def studentborrow():
    if request.method=="POST":
        req = request.form
        status = admin_stu_borrow(req)
        if status == "Success":
            return redirect("/admin")
        else:
            return redirect("/admin/studentborrow")
    return render_template("studentborrow.html")

@app.route("/admin/teacherborrow",methods=["GET","POST"])
def teacherborrow():
    if request.method=="POST":
        req = request.form
        status = admin_teach_borrow(req)
        if status == "Success":
            return redirect("/admin")
        else:
            return redirect("/admin/teacherborrow")
    return render_template("teacherborrow.html")

@app.route("/studentprofile/studetails")
def studetails():
    if "user" in session:
        user = session["user"]
        data = list()
        data = stu_det(user)
        if not data:
            data = [("NULL","NULL","NULL","NULL","NULL")]
    else:
        return redirect("/student_login")
    return render_template("studetails.html",result=data)

@app.route("/teacherprofile/teachdetails")
def teachdetails():
    if "user" in session:
        user = session["user"]
        data = list()
        data = teach_det(user)
        if not data:
            data = [("NULL","NULL","NULL","NULL","NULL")]
    else:
        return redirect("/teacher_login")
    return render_template("teachdetails.html",result=data)

@app.route("/studentprofile/stuupdate",methods=["GET","POST"])
def stuupdate():
    status = None
    if request.method == "POST":
        req = request.form
        status = update(req,session["user"],"s")
        if status == "Success":
            return redirect("/studentprofile")
        else:
            return redirect("/studentprofile/stuupdate")
    return render_template("stuupdate.html")

@app.route("/teacherprofile/teachupdate",methods=["GET","POST"])
def teachupdate():
    status = None
    if request.method == "POST":
        req = request.form
        status = update(req,session["user"],"t")
        if status == "Success":
            return redirect("/teacherprofile")
        else:
            return redirect("/teacherprofile/teachupdate")
    return render_template("teachupdate.html")

@app.route("/studentprofile/stuavailbooks")
def stuavailbooks():
    if "user" in session:
        user = session["user"]
        data = list()
        data = avail_books()
        if not data:
            data = [("NULL","NULL","NULL","NULL")]
    else:
        return redirect("/student_login")
    return render_template("stuavailbooks.html",result=data)

@app.route("/teacherprofile/teachavailbooks")
def teachavailbooks():
    if "user" in session:
        user = session["user"]
        data = list()
        data = avail_books()
        if not data:
            data = [("NULL","NULL","NULL","NULL")]
    else:
        return redirect("/teacher_login")
    return render_template("teachavailbooks.html",result=data)

@app.route("/studentprofile/stuhistory")
def stuhistory():
    if "user" in session:
        user = session["user"]
        data = list()
        data = p_stu_history(user)
        if not data:
            data = [("NULL","NULL","NULL","NULL","NULL")]
    else:
        return redirect("/student_login")
    return render_template("stuhistory.html",result=data)

@app.route("/teacherprofile/teachhistory")
def teachhistory():
    if "user" in session:
        user = session["user"]
        data = list()
        data = p_teach_history(user)
        if not data:
            data = [("NULL","NULL","NULL","NULL","NULL")]
    else:
        return redirect("/teacher_login")
    return render_template("teachhistory.html",result=data)

@app.route("/studentprofile/studelacc")
def studelacc():
    if "user" in session:
        user = session["user"]
        stu_del_acc(user)
    else:
        return redirect("/student_login")
    return render_template("studelacc.html")

@app.route("/teacherprofile/teachdelacc")
def teachdelacc():
    if "user" in session:
        user = session["user"]
        teach_del_acc(user)
    else:
        return redirect("/teacher_login")
    return render_template("teachdelacc.html")

@app.route("/logout")
def logout():
    session.pop("user",None)
    return render_template("logout.html")

@app.errorhandler(404)
def err_404(e):
    return render_template("err_404.html")

if __name__ == "__main__":
    app.run(debug=True,host="localhost",port=5000)
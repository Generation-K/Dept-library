import mysql.connector
import re

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="happyday@1",
    database="library_cse"
)

mycursor = db.cursor()

def stu_val(req):
    name=req["name"]
    usn=req["usn"]
    pno=req["phone"]
    dob=req["dob"]
    email=req["email"]
    password=req["password"]
    cpassword=req["cpassword"]
    email_res = re.match(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$",email)
    pno_res = re.match(r"^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$",pno)
    if not name:
        return "Please enter your name"
    elif not usn:
        return "Please enter your USN"
    elif not pno:
        return "Please enter your phone number"
    elif not dob:
        return "Please enter your Date of Birth"
    elif not email:
        return "Please enter your Email ID"
    elif not password:
        return "Please enter the password"
    elif not cpassword:
        return "Please confirm your password"
    elif password != cpassword:
        return "Password and Confirm password should be same"
    elif len(password)<8:
        return "Password should have atleast 8 characters"
    elif len(pno) != 10:
        return "Invalid Phone Number"
    elif not email_res:
        return "Invalid Email"
    elif not pno_res:
        return "Invalid Phone Number"
    else:
        data = list()
        sql1 = "SELECT usn FROM student_user WHERE usn = %s"
        val1 = (req["usn"].upper(),)
        mycursor.execute(sql1,val1)
        data = mycursor.fetchall()
        if not data:
            sql = "INSERT INTO student_user (usn, name, email, pass, phone, dob, br_no) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            val = (usn.upper(),name,email,password,pno,dob,3)
            mycursor.execute(sql, val)
            db.commit()
            return "Success"
        else:
            return "USN already exists"

def teach_val(req):
    name=req["name"]
    emp=req["empcode"]
    pno=req["phone"]
    dob=req["dob"]
    email=req["email"]
    password=req["password"]
    cpassword=req["cpassword"]
    email_res = re.match(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$",email)
    pno_res = re.match(r"^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$",pno)
    if not name:
        return "Please enter your name"
    elif not emp:
        return "Please enter your Employee Code"
    elif not pno:
        return "Please enter your phone number"
    elif not dob:
        return "Please enter your Date of Birth"
    elif not email:
        return "Please enter your Email ID"
    elif not password:
        return "Please enter the password"
    elif not cpassword:
        return "Please confirm your password"
    elif password != cpassword:
        return "Password and Confirm password should be same"
    elif len(password)<8:
        return "Password should have atleast 8 characters"
    elif len(pno) != 10:
        return "Invalid Phone Number"
    elif not email_res:
        return "Invalid Email"
    elif not pno_res:
        return "Invalid Phone Number"
    else:
        data = list()
        sql1 = "SELECT emp FROM teacher_user WHERE emp = %s"
        val1 = (req["empcode"].upper(),)
        mycursor.execute(sql1,val1)
        data = mycursor.fetchall()
        if not data:
            sql = "INSERT INTO teacher_user (emp, name, email, pass, phone, dob) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            val = (emp.upper(),name,email,password,pno,dob,3)
            mycursor.execute(sql, val)
            db.commit()
            return "Success"
        else:
            return "Emp Code already exists"

def book_val(req):
    bid = req["bookid"]
    name = req["bookname"]
    author = req["author"]
    pub = req["publisher"]
    isbn = req["isbn"]
    result = re.match(r"^(?=(?:\D*\d){10}(?:(?:\D*\d){3})?$)[\d-]+$",isbn)
    if not bid:
        return "Enter Book ID"
    elif not name:
        return "Enter Book Name"
    elif not author:
        return "Enter the Author of the Book"
    elif not pub:
        return "Enter the Publisher of the Book"
    elif not isbn:
        return "Enter the ISBN Code"
    elif not result:
        return "Invalid ISBN Code"
    else:
        data = list()
        sql = "SELECT id FROM books WHERE id = %s"
        val = (req["bookid"].upper(),)
        mycursor.execute(sql,val)
        data = mycursor.fetchall()
        if not data:
            sql1 = "INSERT INTO books (id, name, author, publisher, isbn, avail) VALUES (%s,%s,%s,%s,%s,%s)"
            val1 = (bid.upper(),name,author,pub,isbn,1)
            mycursor.execute(sql1,val1)
            db.commit()
            return "Success"
        else:
            return "Book ID already exists"

def S_logval(req):
    data = list()
    sql = "SELECT email, pass FROM student_user WHERE email = %s"
    val = (req["email"],)
    mycursor.execute(sql,val)
    data = mycursor.fetchall()
    if not data:
        return "Invalid Email"
    elif data[0][1] != req["password"]:
        return "Invalid Password"
    else:
        return "Success"

def T_logval(req):
    data = list()
    sql = "SELECT email, pass FROM teacher_user WHERE email = %s"
    val = (req["email"],)
    mycursor.execute(sql,val)
    data = mycursor.fetchall()
    if not data:
        return "Invalid Email"
    elif data[0][1] != req["password"]:
        return "Invalid Password"
    else:
        return "Success"

def update(req,code,who):
    name = req["name"]
    email = req["email"]
    password = req["pass"]
    cpassword = req["cpass"]
    pno = req["phone"]
    if password != cpassword:
        return "Password and Confirm Password must be same"
    elif not name and not email and not password and not cpassword and not pno:
        return "Success"
    elif email:
        email_res = re.match(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$",email)
        if not email_res:
            return "Invalid Email"
    elif pno:
        pno_res = re.match(r"^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$",pno)
        if not pno_res:
            return "Invalid Phone Number"
    elif len(password)<8:
        return "Password should have atleast 8 characters"
    else:
        if who == "s":
            if name:
                sql = "UPDATE student_user SET name=%s WHERE usn=%s"
                val = (name,code)
                mycursor.execute(sql,val)
                db.commit()
            if email:
                sql = "UPDATE student_user SET email=%s WHERE usn=%s"
                val = (email,code)
                mycursor.execute(sql,val)
                db.commit()
            if pno:
                sql = "UPDATE student_user SET phone=%s WHERE usn=%s"
                val = (pno,code)
                mycursor.execute(sql,val)
                db.commit()
            if password:
                sql = "UPDATE student_user SET pass=%s WHERE usn=%s"
                val = (password,code)
                mycursor.execute(sql,val)
                db.commit()
        if who == "t":
            if name:
                sql = "UPDATE teacher_user SET name=%s WHERE emp=%s"
                val = (name,code)
                mycursor.execute(sql,val)
                db.commit()
            if email:
                sql = "UPDATE teacher_user SET email=%s WHERE emp=%s"
                val = (email,code)
                mycursor.execute(sql,val)
                db.commit()
            if pno:
                sql = "UPDATE teacher_user SET phone=%s WHERE emp=%s"
                val = (pno,code)
                mycursor.execute(sql,val)
                db.commit()
            if password:
                sql = "UPDATE teacher_user SET pass=%s WHERE emp=%s"
                val = (password,code)
                mycursor.execute(sql,val)
                db.commit()
        return "Success"

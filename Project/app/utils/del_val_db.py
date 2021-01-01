import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="happyday@1",
    database="library_cse"
)

mycursor = db.cursor()

def stu_del(req):
    usn=req["usn"]
    if not usn:
        return "Please enter Student USN"
    else:
        data = list()
        sql1 = "SELECT usn FROM student_user WHERE usn = %s"
        val1 = (req["usn"].upper(),)
        mycursor.execute(sql1,val1)
        data = mycursor.fetchall()
        if not data:
            return "USN does not exist"
        else:
            sql2 = "DELETE FROM student_user WHERE usn = %s"
            val2 = (req["usn"].upper(),)
            mycursor.execute(sql2,val2)
            db.commit()
            return "Success"            

def teach_del(req):
    emp=req["emp"]
    if not emp:
        return "Please enter Teacher Emp Code"
    else:
        data = list()
        sql1 = "SELECT emp FROM teacher_user WHERE emp = %s"
        val1 = (req["emp"].upper(),)
        mycursor.execute(sql1,val1)
        data = mycursor.fetchall()
        if not data:
            return "Emp Code does not exist"
        else:
            sql2 = "DELETE FROM teacher_user WHERE emp = %s"
            val2 = (req["emp"].upper(),)
            mycursor.execute(sql2,val2)
            db.commit()
            return "Success"

def book_del(req):
    bid=req["bid"]
    if not bid:
        return "Please enter Book ID"
    else:
        data = list()
        sql1 = "SELECT id FROM books WHERE id = %s"
        val1 = (req["bid"].upper(),)
        mycursor.execute(sql1,val1)
        data = mycursor.fetchall()
        if not data:
            return "Book ID does not exist"
        else:
            sql2 = "DELETE FROM books WHERE id = %s"
            val2 = (req["bid"].upper(),)
            mycursor.execute(sql2,val2)
            db.commit()
            return "Success"

def teach_del_acc(emp):
    sql = "DELETE FROM teacher_user WHERE emp=%s"
    val = (emp.upper(),)
    mycursor.execute(sql,val)
    db.commit()

def stu_del_acc(usn):
    sql = "DELETE FROM student_user WHERE usn=%s"
    val = (usn.upper(),)
    mycursor.execute(sql,val)
    db.commit()
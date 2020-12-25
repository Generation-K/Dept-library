import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="happyday@1",
    database="library_cse"
)

mycursor = db.cursor()

def stu_display():
    data = list()
    mycursor.execute("SELECT usn,name,email,phone,dob FROM student_user")
    data = mycursor.fetchall()
    return data

def teach_display():
    data = list()
    mycursor.execute("SELECT emp,name,email,phone,dob FROM teacher_user")
    data = mycursor.fetchall()
    return data

def book_display():
    data = list()
    mycursor.execute("SELECT id,name,author,publisher,isbn FROM books")
    data = mycursor.fetchall()
    return data

def stu_history():
    data = list()
    sql = "SELECT tid,br_id,b_id,dob,due,dor FROM borrow WHERE s_t=%s"
    val = ("s",)
    mycursor.execute(sql,val)
    data = mycursor.fetchall()
    return data

def teach_history():
    data = list()
    sql = "SELECT tid,br_id,b_id,dob,due,dor FROM borrow WHERE s_t=%s"
    val = ("t",)
    mycursor.execute(sql,val)
    data = mycursor.fetchall()
    return data

def book_history():
    data = list()
    mycursor.execute("SELECT tid,br_id,b_id,dob,due,dor FROM borrow")
    data = mycursor.fetchall()
    return data

def stu_det(usn):
    data = list()
    sql = "SELECT usn,name,email,phone,dob FROM student_user WHERE usn=%s"
    val = (usn,)
    mycursor.execute(sql,val)
    data = mycursor.fetchall()
    return data

def teach_det(emp):
    data = list()
    sql = "SELECT emp,name,email,phone,dob FROM teacher_user WHERE emp=%s"
    val = (emp,)
    mycursor.execute(sql,val)
    data = mycursor.fetchall()
    return data

def avail_books():
    data = list()
    sql = "SELECT id,name,author,publisher FROM books WHERE avail=%s"
    val = (1,)
    mycursor.execute(sql,val)
    data = mycursor.fetchall()
    return data

def p_stu_history(usn):
    data = list()
    sql = "SELECT br_id,b_id,dob,due,dor FROM borrow WHERE br_id=%s"
    val = (usn,)
    mycursor.execute(sql,val)
    data = mycursor.fetchall()
    return data

def p_teach_history(emp):
    data = list()
    sql = "SELECT br_id,b_id,dob,due,dor FROM borrow WHERE br_id=%s"
    val = (emp,)
    mycursor.execute(sql,val)
    data = mycursor.fetchall()
    return data

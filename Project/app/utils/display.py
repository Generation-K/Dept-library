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
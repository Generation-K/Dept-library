import mysql.connector
from datetime import date

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="happyday@1",
    database="library_cse"
)

mycursor = db.cursor()

def admin_stu_borrow(req):
    if not req["usn"]:
        return "Enter USN"
    elif not req["bookid"]:
        return "Enter Book ID"
    elif not req["dob"]:
        return "Enter Borrow Date"
    elif not req["due"]:
        return "Enter Due Date"
    else:
        sql1 = "INSERT INTO borrow (br_id, b_id, dob, due, s_t) VALUES %s,%s,%s,%s,%s,%s"
        val1 = (req["usn"],req["bookid"],req["dob"],req["due"],"s")
        mycursor.execute(sql1,val1)
        db.commit()
        sql2 = "UPDATE books SET avail=0 WHERE id=%s"
        val2 = (req["bookid"],)
        mycursor.execute(sql2,val2)
        db.commit()
        return "Success"

def admin_teach_borrow(req):
    if not req["emp"]:
        return "Enter EMP Code"
    elif not req["bookid"]:
        return "Enter Book ID"
    elif not req["dob"]:
        return "Enter Borrow Date"
    elif not req["due"]:
        return "Enter Due Date"
    else:
        sql1 = "INSERT INTO borrow (br_id, b_id, dob, due, s_t) VALUES %s,%s,%s,%s,%s,%s"
        val1 = (req["emp"],req["bookid"],req["dob"],req["due"],"t")
        mycursor.execute(sql1,val1)
        db.commit()
        sql2 = "UPDATE books SET avail=0 WHERE id=%s"
        val2 = (req["bookid"],)
        mycursor.execute(sql2,val2)
        db.commit()
        return "Success"

def returnbook(req):
    if not req["code"]:
        return "Enter Borrower Code"
    elif not req["bookid"]:
        return "Enter BookID"
    elif not req["dor"]:
        return "Enter Return Date"
    else:
        sql = "UPDATE borrow SET dor=%s WHERE br_id=%s AND b_id=%s AND dor=NULL"
        val = (req["dor"],req["code"],req["bookid"])
        mycursor.execute(sql,val)
        db.commit()
        sql1 = "UPDATE books SET avail=1 WHERE id=%s"
        val1 = (req["bookid"])
        mycursor.execute(sql1,val1)
        return "Success"
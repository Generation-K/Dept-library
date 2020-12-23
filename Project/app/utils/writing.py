import csv

def stu_write(entries):
    with open("C:\\Users\\Sharan\\Downloads\\Student_Users.csv", "w", newline="") as f:
        fieldnames = ["USN","Name","Email ID","Phone Number","DOB"]
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        writer.writeheader()
        for i in entries:
            writer.writerow({ "USN":i[0], "Name":i[1], "Email ID":i[2], "Phone Number":i[3], "DOB":i[4] })

def teach_write(entries):
    with open("C:\\Users\\Sharan\\Downloads\\Teacher_Users.csv", "w", newline="") as f:
        fieldnames = ["Emp Code","Name","Email ID","Phone Number","DOB"]
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        writer.writeheader()
        for i in entries:
            writer.writerow({ "Emp Code":i[0], "Name":i[1], "Email ID":i[2], "Phone Number":i[3], "DOB":i[4] })

def book_write(entries):
    with open("C:\\Users\\Sharan\\Downloads\\Book.csv", "w", newline="") as f:
        fieldnames = ["Book ID","Name","Author","Publisher","ISBN Code"]
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        writer.writeheader()
        for i in entries:
            writer.writerow({ "Book ID":i[0], "Name":i[1], "Author":i[2], "Publisher":i[3], "ISBN Code":i[4] })

def stu_history_csv(data):
    with open("C:\\Users\\Sharan\\Downloads\\Students_history.csv", "w", newline="") as f:
        fieldnames = ["Tid","Borrower","Book ID","Date of Borrow","Due Date","Date of Return"]
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        writer.writeheader()
        for i in data:
            writer.writerow({ "Tid":i[0], "Borrower":i[1], "Book ID":i[2], "Date of Borrow":i[3], "Due Date":i[4], "Date of Return":i[5] })
    

def teach_history_csv(data):
    with open("C:\\Users\\Sharan\\Downloads\\Teachers_history.csv", "w", newline="") as f:
        fieldnames = ["Tid","Borrower","Book ID", "Date of Borrow","Due Date","Date of Return"]
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        writer.writeheader()
        for i in data:
            writer.writerow({ "Tid":i[0], "Borrower":i[1], "Book ID":i[2], "Date of Borrow":i[3], "Due Date":i[4], "Date of Return":i[5] })

def book_history_csv(data):
    with open("C:\\Users\\Sharan\\Downloads\\Books_history.csv", "w", newline="") as f:
        fieldnames = ["Tid","Book ID","Borrower","Date of Borrow","Due Date","Date of Return"]
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        writer.writeheader()
        for i in data:
            writer.writerow({ "Tid":i[0], "Borrower":i[1], "Book ID":i[2], "Date of Borrow":i[3], "Due Date":i[4], "Date of Return":i[5] })
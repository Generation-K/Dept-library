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
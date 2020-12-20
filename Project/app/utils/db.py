def insert(req):
    name=req["name"]
    usn=req["usn"]
    pno=req["phone"]
    dob=req["dob"]
    email=req["email"]
    password=req["password"]
    cpassword=req["cpassword"]
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
    else:
        return "Success"
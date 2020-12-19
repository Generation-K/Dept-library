def logval(req):
    email=req["email"]
    password=req["password"]
    if not email:
        return "Please enter your Email ID"
    elif not password:
        return "Please enter the password"
    else:
        return "Success"
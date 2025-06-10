# Correct email address - tulasi@gmail.com
#Correct Password - 12345

email = input("Enter your email address:")


if '@' in email :
    password = input("Enter you password")
    if email == "tulasi@gmail.com" and password == "12345" :
        print("Welcome") 
    elif email == "tulasi@gmail.com" and password!="12345" :
        print("Enter the correct password")
        password = input("Enter the corrected password")
        if password == "12345" :
            print("Correct Password");
            print("Welcome")
        else:
            print("Still the password is incorrect")
    elif email != "tulasi@gmail.com" and password=="12345" :
        print("Emailis incorrect")
        email = input("Enter the correct email");
        if email == "tulasi@gmail.com" :
            print("Correct Email Address");
            print("Welcome")
        else:
            print("Still the email address is incorrect")
    else :
        print("Incorrect credentials")
else :
    print("Entered email is in correct")


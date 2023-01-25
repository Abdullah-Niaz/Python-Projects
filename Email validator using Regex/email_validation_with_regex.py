import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
user_email = input("Enter your Email: ")

if re.search(regex, user_email):
    print("Right Email ")
else:
    print("Wrong Email ")

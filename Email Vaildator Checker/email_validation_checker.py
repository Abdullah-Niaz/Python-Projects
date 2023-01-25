email = input("Enter your E-mail ")
k, j, d = 0, 0, 0
# Check the length of the Email
# It should be greater than
if len(email) >= 6:
    #  Email should start with Alpha letters
    if email[0].isalpha():
        # At least one @ in email
        if ('@' in email) and (email.count('@') == 1):
            # . in email should be at 3 or 4th position accor to domain of .com & .in
            if (email[-3] == '.') ^ (email[-4] == '.'):
                # Run the for loop to verify. There's no space in the text
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif i.isspace():
                        j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "@" or i == ".":
                        continue
                    else:
                        d == 1
                if k == 1 or j == 1:
                    print("Wrong Email at step 5")
                else:
                    print("Right Email, you can go with this one")
            else:
                print("Wrong Email at step 4")
        else:
            print("Wrong Email At Step 3")
    else:
        print("Wrong Email At Step 2")
else:
    print("Wrong Email At Step 1")

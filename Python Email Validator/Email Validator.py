email = input("Enter your email : ")

if len(email) < 6:
    print("Not an email address")
    print("Email can't be less than 6 characters")

elif not email[0].isalpha():
    print("Not an email address")
    print("First letter must be an alphabet")

elif ("@" not in email) or (email.count("@") != 1):
    print("Not an email address")
    print("Checkout the @ symbol")

elif email[-4] != "." and email[-3] != ".": 
    print("Not an email address")
    print("Wrong postfix")

elif " " in email:
    print("Not an email address")
    print("There must be no spaces between")

else:
    print("Perfect Email : ", email)

for i in email:
    if i.isupper():
        print("Not an email address")
        print("There must be no capital letters")
        break
    
    elif not i.isalpha():
        if not i.isnumeric():
            if (i != "_") and (i != "@") and (i != ".") :
                print("Not an email address")
                print("No special characters allowed except _ . and @")
                break

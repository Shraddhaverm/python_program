firstname=input("enter your first name:-")
lastname=input("eneter your last name:-")
if(firstname=="shravi" and lastname=="verma"):
    print("correct name")
    password=int(input("eneter your password"))
    if(password>=0-9 or password<="a-z" or password==("@%*")):
        print("correct password")
        language=input("enter your language")
        if(language=="english" or "hindi"):
            print("correct")
            number=int(input("enter your number"))
            if(number>=0 or number<=9):
                print("correct number")
                print("enter your gender")
                ch=input("enter your choice")
                if(ch=="male" or "female" or"transgender"):
                    print("login successful")
                else:
                    print("invalid login") 

            else:
                print("incorrect number")
        else:
            print("incorrect")
    else:
        print("incorrect password")
else:
    print("not correct")

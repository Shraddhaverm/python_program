print("please insert your credit card")
language=input("enter your langusge:")
pin=int(input("enter your pin:"))
if(language=="english" or "hindi")and(pin==1234):
    print("login seccessful")
    ch=int(input("enter your choice"))
    if(ch==1):
      print("enter your debit")
    
    elif(ch==2):
            print("enter your credit")
    elif(ch==3):
        print("enter your widraw")
        amount=int(input("enter your amount"))
        if (amount>=500 and amount<=40000):
            print("please take your amount form check box")
    
        else:
            print("amount is min 500 and max 40000")
    else:
        print("wrong ch")    


else:
    print("invalid login")

print("thank you")
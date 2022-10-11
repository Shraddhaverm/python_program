print("please insert your credit card")
language=input("enter your langusge:")
pin=int(input("enter your pin:"))
if(language=="english" or "hindi")and(pin==1234):
   print("login successful")
   ch=int(input("enter your choice"))
   if(ch==1):
      print("enter your debit")
      amount=int(input("enter you debit case"))
      if(amount>=1 and amount<=500000):
          print("case debited")
      else:
            print("case is not debited")
   elif(ch==2):
        print("enter your credit")
        amount=int(input("enter you credit case"))
        if(amount>=1 and amount<=500000):
           print("case credited")
        else:
          print("case is not credited")
   elif(ch==3):
        print("enter your widraw")
        amount=int(input("enter your amount"))
        if (amount>=500 and amount<=40000):
            print("please take your amount form check box")
    
        else:
            print("amount is min 500 and max 40000")
   else:
         print("wrong choice")

        
else:
    print("invalid login")
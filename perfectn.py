from re import I


n=int(input("enter a number"))
i=1
s=0
while i<n:
    if (n%i==0):
        s=s+i
        i=i+1
    if(s==n):
      print("this is perfect number")
    else:
      print("this is not perfect number")
    

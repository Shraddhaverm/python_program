def sumofdigit(n):
    sum=0
    i=0
    rem=0
    while n>0:
        rem=n%10
        sum=sum+rem*rem
        n=n//10
        return sum
n=int(input("enter any number"))
result=n
while (result!=1 and result!=4):
    result=sumofdigit(result)
    i=i+1
    if result==1:
        print(n,"is happy number")
    else:
        print(n,"is not happy number")

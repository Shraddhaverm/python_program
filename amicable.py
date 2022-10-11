x=int(input('Enter first number :'))  
y=int(input('Enter second number :'))  
sum1=0  
sum2=0  
for i in range(1,(x//2)+1):  
    if x%i==0:  
        sum1+=i  
for j in range(1,(y//2)+1):  
    if y%j==0:  
        sum2+=j  
if(sum1==y and sum2==x):  
    print('Given numbers are Amicable!')  
else:  
    print('Given numbers are not Amicable!')  
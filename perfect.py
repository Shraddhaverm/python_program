n = int(input("Enter any number: "))
i=1
s=0
while i<n:
    if(n%i==0):
        s=s+i
        i=i+1
if (s==n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")
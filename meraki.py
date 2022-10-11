i=0
while i<100:
    print(i)
    if(i%3==0):
        print("nav")
        if(i%7==0):
            print("gurukul")
            if(i%3==0 and i%7==0):
                print("navgurukul")
    i=i+1
print("thanks")
#write a program which will keep adding a stream of number's inputed by the user the adding stop as soon as user presses q key on the keyboard


sum=0
while(True):
    userinput =input("enter the item price or press q to quite:\n")
    if (userinput!='q'):
        sum=sum+int(userinput)
        print(f"order total so far:{sum}")
    else:
            print(f"your total is {sum}.tanks for shopping with us")
            break

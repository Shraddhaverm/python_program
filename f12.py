for x in range(1,6):
    for y in range(1,6):
        if(x==y or y+x==6):
            print("*",end="")
        else:
            print("  ",end="")
    print()       


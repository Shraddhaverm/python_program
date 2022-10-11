def fact(n):
    if n==1:
        return n
    return n* fact(n-1) 


def permutation(n,r):
    return fact(n)/fact(n-r)
   

def combination(p,q):
    return fact(p)/fact(p-q)*fact(q)

print(permutation(8,5))
print(combination(8,5))

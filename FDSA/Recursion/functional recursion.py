#print sum of n numbers using functional recursion
def sup(n) :
    if n==1 :
        return 1

    return n + sup(n-1)

n=int(input("enter value for n"))
print(sup(n))

#factorial of number using recursion

def fac(n) :
    if n==1 :
        return 1
    return n*fac(n-1)
n=int(input("enter value for n"))
print(fac(n))


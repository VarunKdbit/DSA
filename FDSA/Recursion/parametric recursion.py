def greet(n) :
    if n>=1 :
        print("Hello Anirudh")
    else :
        return
    greet(n-1)


n=int(input("Enter the times you wanna print Hello Anirudh"))
print(greet(n))

#print 1 to n using recursion

def pn1toN(i,n) :
    if i>n :
        return 
    
    print(i)
    pn1toN(i+1,n)

n=int(input("Enter the number "))
print(pn1toN(1,n))

#sum of numbers from 1 to n 

def sumofn(s,n) :
    if n<=0 :
        print(s)
        return 
    s+=n
    sumofn(s,n-1)

n=int(input("Enter the number "))
print(sumofn(0,n))



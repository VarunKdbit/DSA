def greet(n) :
    if n>=1 :
        print("Hello Anirudh")
    else :
        return
    greet(n-1)


n=int(input("Enter the times you wanna print Hello Anirudh"))
print(greet(n))

#print 1 to n using recursion
n=int(input("Enter the number "))
def pov(n) :
    
    if n == 0:
        return
    print(n)
    pov(n-1) 
    print(n)

print(pov(n))


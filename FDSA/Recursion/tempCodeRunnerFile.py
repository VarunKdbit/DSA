n=int(input("Enter the number "))
def pov(n) :
    
    if n == 0:
        return
    print(n)
    pov(n-1) 
    print(n)

print(pov(n))

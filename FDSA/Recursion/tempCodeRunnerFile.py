n=int(input("Enter the number "))
l=[]
def pov(n,l) :
    l.append(n)
    if n >=1 :
        print(n)
    else :
        return
    pov(n-1,l) 

print(pov(n,l))

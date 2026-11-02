def pn1toN(i,n) :
    if i>n :
        return 
    
    print(i)
    pn1toN(i+1,n)

n=int(input("Enter the number "))
print(pn1toN(1,n))

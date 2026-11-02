def sumofn(s,n) :
    if n<=0 :
        print(s)
        return 
    s+=n
    sumofn(s,n-1)

n=int(input("Enter the number "))
print(sumofn(0,n))


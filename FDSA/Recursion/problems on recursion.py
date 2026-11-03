# reverse array using recursion 
a=[5,6,8,12,14,3,1,4]
i=0
j=7
def rev(a,i,j) :
    if j<=i:
        return a
    a[i],a[j]=a[j],a[i]
    return rev(a,i+1,j-1)

print(rev(a,i,j))

# Check if the string is palindrome or not 
st="asvs"
def cp(i,j,st) :
    if j<=i :
        print("true")
        return 
    if st[i]!=st[j] :
        print("false")
        return
    cp(i+1,j-1,st) 
print(cp(0,len(st)-1,st))


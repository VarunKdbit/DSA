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
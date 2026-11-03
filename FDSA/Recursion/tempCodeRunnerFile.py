st="asvs"
def cp(i,j,st) :
    if j<=i :
        return True
    if st[i]!=st[j] :
        return False
    cp(i+1,j-1,st) 
print(cp(0,len(st)-1,st))
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
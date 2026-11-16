n=  len(a)
for i in range (n-2,-1,-1):
    for j in range(0,i) :
        if j[a]>j+1[a] :
            a[j], a[j+1] = a[j+1],a[j]
            

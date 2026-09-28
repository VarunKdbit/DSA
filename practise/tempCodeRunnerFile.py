a=[5,6,5,1,2,1,1,3]
freak = {}
for i in a :
    freq=1
    for j in range (i,len(a)) :
        if a[i]==j:
            freq+=1
    freak[i]= freq 

print(freak)

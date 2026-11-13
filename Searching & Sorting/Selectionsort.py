#sort an array in ascending order using selectionsort
ar=[64,67,1,2,5,7,0,8]
n=len(ar)
for i in range (0,n) :
    min=ar[i]
    for j in range (i+1,n) :
        if ar[j]<ar[i] :
            min=ar[j]
            ar[j],ar[i]=ar[i],ar[j]
print(ar)
#Time Complexity : O(n^2)
#Space Complexity : O(1)


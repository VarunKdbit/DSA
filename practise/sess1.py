n=[1,3,5,6,5,4,5,3,10]
m=[1,5,113,95,4]

l=114

hash_list=[0] * l

for i in n :
    hash_list[i] +=1

for j in m :
    print(j,hash_list[j])
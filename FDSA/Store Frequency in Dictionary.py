Freq={}
nums=[1,4,7,6,1,3,5,6,7]
n=len(nums)
for i in range (0,n) :
    Freq[nums[i]]=Freq.get(nums[i],0) + 1
    
print(Freq)

     

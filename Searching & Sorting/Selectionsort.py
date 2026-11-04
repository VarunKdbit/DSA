#sort an array in ascending order using selectionsort
def selectionsort(nums) :
    n=len(nums)
    for i in range (0,n) :
        min_idx = i
        for j in range(i+1,n) :
            if nums[j]<nums[min_idx] :
                min_idx=j
        nums[i],nums[min_idx]=nums[min_idx],nums[i]
    return nums

nums=[5,6,1,3,8,9,0,2]
print(selectionsort(nums))


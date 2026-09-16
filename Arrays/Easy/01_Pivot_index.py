def pivot_index(nums):
    total = sum(nums)
    left_sum = 0

    for i in range(len(nums)) :
        right_sum = total - left_sum - nums[i]

        print("i=",i,"left =",left_sum,right_sum)

        if left_sum == right_sum :
            return i
        
        left_sum +=nums[i]

    return -1

nums = [14,6,7,2,1]
print(pivot_index(nums))

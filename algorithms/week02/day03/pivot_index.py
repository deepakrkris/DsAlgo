
"""
   eg: [1,7,3,6,5,6]
"""
def pivot_index(nums) :

    left_r_sum = [0]
    right_r_sum = [0]

    for i in range(1, len(nums)) :
        left_r_sum.append(left_r_sum[-1] + nums[i - 1])
        right_r_sum.append(right_r_sum[-1] + nums[len(nums) - i])

    right_r_sum = right_r_sum[::-1]

    for i in range(len(nums)) :
        if left_r_sum[i] == right_r_sum[i] :
            return i

    return - 1

print(pivot_index([1,7,3,6,5,6]))
print(pivot_index([1,2,3]))
print(pivot_index([2,1,-1]))

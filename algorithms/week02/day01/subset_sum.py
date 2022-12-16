def can_partition_array(nums):
    
    def sum_of_numbers(index, sum1, sum2) :
        if index == len(nums) and sum1 == sum2 :
            return True
        
        if index == len(nums) :
            return False
        
        add_to_sum1 = sum_of_numbers(index + 1, sum1 + nums[index], sum2)
        add_to_sum2 = sum_of_numbers(index + 1, sum1, sum2 + nums[index])
        return add_to_sum1 or add_to_sum2

    return sum_of_numbers(0, 0, 0)

def partition_array_recursive(nums):
    
    def sum_of_numbers(index, sum1, sum2) :
        if index < 0 and sum1 == sum2 :
            return True
        
        if index < 0 :
            return False

        add_to_sum1 = sum_of_numbers(index - 1, sum1 + nums[index], sum2)
        add_to_sum2 = sum_of_numbers(index - 1, sum1, sum2 + nums[index])
        return add_to_sum1 or add_to_sum2

    return sum_of_numbers(len(nums) - 1, 0, 0)

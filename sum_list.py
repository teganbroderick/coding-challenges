#sum a list using recursion

def sum_list(nums):
    """Using recursion, return the sum of numbers in a list."""


    if nums == []:
        return 0
    
    return nums[0] + sum_list(nums[1:])

print(sum_list([-5, 10, 4]))
def show_evens(nums):
    """Given list of ints, return list of *indices* of even numbers in list."""
    indices_list = []
    for i in range (0, len(nums)):
        if nums[i] % 2 == 0:
            indices_list.append(i)
    return indices_list

print(show_evens([1, 2, 3, 4, 6, 8]))
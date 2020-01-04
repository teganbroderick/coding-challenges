


def mode(nums):
    """Find the most frequent num(s) in nums."""

    mode_dict = {}

    for num in nums:
        if mode_dict.get(num) == None:
            mode_dict[num] = 1
        else:
            mode_dict[num] += 1
    print("mode_dict", mode_dict)

    highest_count = max(mode_dict.values())
    print("highest_count", highest_count)

    count_set = set()

    for key, value in mode_dict.items():
        if value == highest_count:
            count_set.add(key)

    return count_set

print(mode([1, 2, 2, 3]))
print(mode([1, 1, 2, 2]))
print(mode([1]))

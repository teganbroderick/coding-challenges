def find_repeat(numbers):

    # Find a number that appears more than once
    seen_set = set()
    nums_seen_multiple_times = []
    for num in numbers:
        if num not in seen_set:
            seen_set.add(num)
        else:
            nums_seen_multiple_times.append(num)
    return nums_seen_multiple_times[0]
    
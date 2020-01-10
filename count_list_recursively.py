def count_recursively(lst):
    """Return number of items in a list, using recursion."""
    if lst == []:
        return 0

    count = 1 + count_recursively(lst[1:])
    return count

print(count_recursively([]))
print(count_recursively([1, 2, 3]))
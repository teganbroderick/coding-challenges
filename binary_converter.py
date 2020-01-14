def find_binary(num):
    """return binary values for input nums"""
    binary_list = []
    while num != 0:
        val = num % 2
        if val == 1: #if odd
            binary_list.append(1)
            num = num // 2
        else: #if even
            binary_list.append(0)
            num = num // 2
    binary_list.reverse()
    return binary_list

print(find_binary(4))
print(find_binary(1))
def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome
    #if empty string return True immediately
    if len(the_string) == 0:
        return True
    
    char_count_dict = {}
    for char in the_string:
        if char not in char_count_dict.keys():
            char_count_dict[char] = 1
        else:
            char_count_dict[char] += 1
            
    print(char_count_dict)

    #count amount of odd values in dict, if num of odd vals is even, return false
    odd_count = 0
    for value in char_count_dict.values():
        if value % 2 != 0:
            odd_count += 1
            
    return odd_count <= 1
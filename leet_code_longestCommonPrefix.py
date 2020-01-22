def longestCommonPrefix(strs):      
    """return longest common prefix string among an array of strings"""
    
    if strs == []:
        return ""

    #find shortest_length
    shortest_length = len(strs[0])
    for word in strs:
        if len(word) < shortest_length:
            shortest_length = len(word)
    print(shortest_length)

    word_to_compare = strs.pop()
    prefix_list = []

   
    for i in range(shortest_length):
        letter_to_compare = word_to_compare[i]
        # print(letter_to_compare)
        matches = 0
        for j in range(len(strs)):
            # print(strs[j][i])
            if strs[j][i] == letter_to_compare:
                matches += 1

        if matches == len(strs):
            prefix_list.append(letter_to_compare)
        else:
            break

    prefix_string = "".join(prefix_list)
    return prefix_string


print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["aca","cba"]))

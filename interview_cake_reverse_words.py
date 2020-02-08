def reverse_words(message):

    # Decode the message by reversing the words
    #first: reverse letters in list in place
    reversed_char_message = reverse_chars(message)
    # print(reversed_char_message)

        
    #second: reverse each word
    current_start = 0
    for i in range(0, len(reversed_char_message)):
        #if we hit a space, reverse chars up to that space
        if reversed_char_message[i] == " ":
            reversed_char_message[current_start: i] = reverse_chars(reversed_char_message[current_start:i])
            current_start = i+1
        #if we get to the end of the list, reverse last word
        elif i == (len(reversed_char_message) - 1):
            reversed_char_message[current_start: i+1] = reverse_chars(reversed_char_message[current_start:i+1])
    # print(reversed_char_message)
    return reversed_char_message
            

def reverse_chars(message):
    """reverse chars in a list in place"""
    
    for i in range(0, (len(message) // 2)):
        char_a = message[i]
        char_b = message[-i-1]
        message[i] = char_b
        message[-i-1] = char_a
    return message

print(reverse_words([ 'c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l' ]))
# print(reverse_list([ 'c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l' ]))



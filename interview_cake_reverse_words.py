def reverse_words_in_string(char_list):
    """reverse words in a list in place"""

    #reverse chars in list
    reversed_list = reverse_list(char_list, 0, len(char_list) -1)
    #words will be in the right place, but chars will be reversed
    #reverse each individual word
    print(reversed_list)
    
    front_index = 0
    
    for i in range(0, len(reversed_list)):
        if (i == len(reversed_list)) or (reversed_list[i] == ' '):
            print(reversed_list[front_index:i])
            reverse_list(reversed_list, front_index, i-1)
            front_index = i + 1

    return reversed_list

def reverse_list(char_list, front_index, end_index):
    """reverse a list of characters in place"""

    while front_index < end_index: 
        char_at_front = char_list[front_index]
        # print("char at front", char_at_front)
        char_at_end = char_list[end_index]
        # print("char at end", char_at_end)

        char_list[front_index] = char_at_end
        char_list[end_index] = char_at_front

        front_index += 1
        end_index -= 1

    return char_list

print(reverse_words_in_string([ 'c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l' ]))
# print(reverse_list([ 'c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l' ]))


# def reverse_words(message):
#     # First we reverse all the characters in the entire message
#     message2 = reverse_characters(message, 0, len(message)-1)

#     # This gives us the right word order
#     # but with each word backward

#     # Now we'll make the words forward again
#     # by reversing each word's characters

#     # We hold the index of the *start* of the current word
#     # as we look for the *end* of the current word
#     current_word_start_index = 0

#     for i in range(len(message2) + 1):
#         # Found the end of the current word!
#         if (i == len(message2)) or (message2[i] == ' '):
#             reverse_characters(message2, current_word_start_index, i - 1)
#             # If we haven't exhausted the message our
#             # next word's start is one character ahead
#             current_word_start_index = i + 1

#     return message2

# def reverse_characters(message, left_index, right_index):
#     # Walk towards the middle, from both sides
#     while left_index < right_index:
#         # Swap the left char and right char
#         message[left_index], message[right_index] = \
#             message[right_index], message[left_index]
#         left_index  += 1
#         right_index -= 1
#     return message

# print(reverse_words([ 'c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l' ]))

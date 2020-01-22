def isPalindrome(x):
    """return True if integer is a palindrome"""
    
    #list of chars
    int_as_str = str(x)
    int_list = list(int_as_str)
    
    #reversed list of chars
    int_list_2 = list(int_as_str)
    int_list_2.reverse()


    
    if int_list == int_list_2:
        return True
    else:
        return False

print(isPalindrome(-121))
#in => positive integer
#add its digits until you get one integer
#out => int

"""
example:
in => 38
3 + 8 = 11
1 + 1 = 2
out => 2
"""

#base case => len(intstring) == 1
#convert int to str
#split str into list
#add all digits of list
#convert back to intstr

def add_digits(integer):
    """add digits of int until you have one number, recursively"""

    #base case => len(intstring) == 1
    int_string = str(integer)
    
    if len(int_string) == 1:
        return integer
        
    sum_ints = 0
    for char in int_string:
        sum_ints += int(char)
    # print(sum_ints)
    
    return add_digits(sum_ints)
    
print(add_digits(38))
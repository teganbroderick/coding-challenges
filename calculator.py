#polish notation calculator


def calculator(str):
    """using polish notation to do calculation in string"""

    nums = list(1234567890)
    operators = list(+-/*)

    chars = list(nums)
    
    char1 = chars[-1]
    sum = 0
    operator = 0
    
    while chars != []:
        


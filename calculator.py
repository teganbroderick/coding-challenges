#polish notation calculator
#eg. 1+2 => +12


def calculator(str1):
    """using polish notation to do calculation in string"""

    nums = ["1","2","3","4","5","6","7","8","9","0"]
    operators = list("+-/*")

    chars = str1.split(" ")
    
    result = int(chars[-1])
    # print(type(result))
    chars.pop()
    # print(chars)
    
    while chars != []:
        char_to_assess = chars.pop()
        # print("char to assess", char_to_assess)
        
        #if char is a number, assign number to a variable       
        if char_to_assess in nums:
            char1 = int(char_to_assess)
        
        #if char is an operator, perform operation
        elif char_to_assess in operators:
            if char_to_assess == "+":
                result = char1 + result
            elif char_to_assess == "-":
                result = char1 - result
            elif char_to_assess == "*":
                result = char1 * result
            elif char_to_assess == "/":
                result = char1 /result
    
        # print("result", result)
    return result


print(calculator("/ 6 - 4 2"))
print(calculator("+ 1 2"))
print(calculator("- 9 * 2 3"))
print(calculator("+ 9 * 2 3"))
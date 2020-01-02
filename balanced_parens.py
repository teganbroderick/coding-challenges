#Given a string, return True or False depending on whether that string has balanced parentheses.

def is_balanced(string):
    """return True or False depending on whether that string has balanced parentheses"""

    num_opening = 0
    num_closing = 0

    for char in string:
        if char == "(":
            num_opening += 1
        elif char == ")":
            num_closing += 1

    if num_opening == num_closing:
        return True
    else:
        return False


print(is_balanced("(This has (too many closes.) ) )"))
print(is_balanced("()"))
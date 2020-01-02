#Given a string, return True or False depending on whether the string’s opening-and-closing marks (that is, brackets) are balanced.

def is_balanced(string):
    """return true if string contains balanced brackets"""

    brackets_opening = ["(", "[", "<", "{"]
    brackets_closing = [")", "]", ">", "}"]

    bracket_dict = {
        "(": ")",
        "[":"]",
        "<":">",
        "{":"}"
    }
    seen_list = []
    for char in string:
        if char in brackets_opening:
            seen_list.append(char)

        if char in brackets_closing:
            char_to_compare = seen_list[-1]
            if bracket_dict[char_to_compare] == char:
                seen_list.pop()
            else:
                return False
    if seen_list == []:
        return True



print(is_balanced("<ok>"))

print(is_balanced("{[[This has too many open square brackets.]}"))

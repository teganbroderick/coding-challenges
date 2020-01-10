def rev_string(astring):
    """Return reverse of string using recursion.

    You may NOT use the reversed() function!
    """
    if len(astring) < 2:
        return astring
    
    return astring[-1] + rev_string(astring[:-1])


print(rev_string("porcupine"))

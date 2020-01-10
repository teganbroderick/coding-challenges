def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses."""

    assert 0 < val < 101, "Val must be between 1-100"

    num_guesses = 0

    number = 100
    remainder = 100

    while number != val:

        if val < number:
            # print(number)
            # print("remainder", remainder)
            num_guesses += 1
            remainder = remainder // 2
            number = number - remainder
        else:
            num_guesses += 1
            # print("num", number)
            # print("remainder", remainder)
            remainder = remainder // 2
            number = number + remainder

    return num_guesses

print(binary_search(50))
print("")
print(binary_search(31))
print("")
print(binary_search(25))
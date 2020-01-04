#given a muber, print digits backwards"""

def print_digits(num):

    num = str(num)
    num_list = list(num)

    for i in range(len(num_list)-1, -1, -1):
        print(num_list[i])

print_digits(12)
print_digits(314)
print()

#given a muber, print digits backwards using maths"""

def print_digits_maths(num):
    """print digits of number backwards"""

    str_num = str(num)
    for i in range(0, len(str_num)):

        last_digit = num % 10
        print(last_digit)

        num = num // 10

print_digits_maths(12)
print_digits_maths(314)
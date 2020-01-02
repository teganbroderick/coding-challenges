#is prime number

def is_prime_number(num):
    """return true if number is prime, return false if not"""

    for i in range(2, num):
        if num % i == 0:
            return False
        else:
            return True

print(is_prime_number(11))
print(is_prime_number(2))
print(is_prime_number(6))
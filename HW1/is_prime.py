# Hunter Scheppat | Logic & Computation | Fall 2023

import math


# determine if any n is prime
def is_prime(n):
    # determine even/odd first
    if n < 2:
        return False
    # check every num up to square root
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

# main function logic
if __name__ == "__main__":
    while True:
        num = int(input('> '))
        print(is_prime(num))


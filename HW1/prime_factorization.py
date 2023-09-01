# Hunter Scheppat | Logic & Computation | Fall 2023

import math
from is_prime import is_prime


# get the prime factorization of any n
def prime_factorization(n):
    # instantiate array of factors
    factors = []

    # check if n is already prime
    if is_prime(n):
        factors.append(n)
        return factors

    # check every num up to square root
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            while n % i == 0:
                # append the prime & divide by it
                factors.append(int(i))
                n /= i

            # if left with a prime, append and return
            if is_prime(n):
                factors.append(int(n))
                return factors

    # return all factors at end of loop
    return factors


# main function logic
if __name__ == "__main__":
    while True:
        num = int(input('> '))
        print(prime_factorization(num))


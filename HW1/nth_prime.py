# Hunter Scheppat | Logic & Computation | Fall 2023

from is_prime import is_prime

# hold known primes
primes = {1: 2}


# find nth prime
def nth_prime(n):
    # check dictionary for prime first
    if n in primes:
        return primes.get(n)
    # count up until desired prime
    else:
        # start from the greatest known prime
        counter = max(primes)
        prime = primes.get(counter)

        # increment counter until at desired n
        while counter < n:
            prime += 1
            # add each found prime along the way
            if is_prime(prime):
                counter += 1
                primes[counter] = prime

        # return the nth prime
        return primes.get(counter)

# main function logic
if __name__ == "__main__":
    while True:
        num = int(input('> '))
        print(nth_prime(num))

        
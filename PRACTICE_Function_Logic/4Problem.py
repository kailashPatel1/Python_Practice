# 4. Create a function to check prime numbers in a range.

def primes_in_range(start, end):
    primes = []

    for num in range(start, end + 1):
        if num > 1:   # prime numbers are > 1
            is_prime = True

            for i in range(2, int(num**2) + 1):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                primes.append(num)

    return primes

print(primes_in_range(10, 50))



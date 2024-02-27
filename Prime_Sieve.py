# This program uses the Sieve of Eratosthenes to find all prime numbers up to a given number.

def prime_sieve(n):
    # Create a list of booleans to represent whether a number is prime or not.
    sieve = [True] * (n + 1)

    # 0 and 1 are not prime numbers.
    sieve[0:2] = [False, False]

    # Create a list to store the prime numbers.
    primes = []
    
    # Loop through the numbers and mark the multiples of each number as not prime.
    for i in range(2, n + 1):
        if sieve[i]:
            primes.append(i)
            # Mark the multiples of the current number as not prime.
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    
    return primes

def main():
    n = int(input("Enter A Number To Find All Primes Up To It:\n\n>>> "))
    primes = prime_sieve(n)
    print(f"\nThe Prime Numbers Up To {n} Are:\n{primes}")

if __name__ == "__main__":
    main()
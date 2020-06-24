# This example is taken from Jeff Knupp's excellent blog post on
# generators and the 'yield' keyword. Specifically using the send
# keyword to run coroutines. 

# Source - https://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/

def print_successive_primes(iterations, base=10):
    # like normal functions, a generator function
    # can be assigned to a variable
    prime_generator = get_primes(base)
    prime_generator.send(None)
    for power in range(iterations):
        print(prime_generator.send(base ** power))

def get_primes(number):
    while True:
        if is_prime(number):
            number = yield number
        number += 1

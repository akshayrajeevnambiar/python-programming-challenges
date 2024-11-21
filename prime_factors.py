# Python Code Challenge #1: Find Prime Factors
# ----------------------------------------------
# Your goal is to implement a function, get_prime_factors(), that takes an integer value as the input argument and returns a list containing all of its prime factors.

import math

def get_prime_factors(num):
    
    prime_factors = []
    
    # STEP 1: While num is divisible by 2, print 2 and divide n by 2.
    while num % 2 == 0:
        prime_factors.append(2)
        num /= 2
    
    # STEP 2: After step 1, n must be odd. Now start a loop from i = 3 to the square root of n. 
    # While i divides n, print i, and divide n by i. After i fails to divide n, 
    # increment i by 2 and continue.
    for i in range(3, math.floor(math.sqrt(num) + 1), 2):
        while num % i == 0:
            prime_factors.append(i)
            num /= i
    
    # STEP 3: If n is a prime number and is greater than 2, then n will not become 1 by the above two steps. So print n if it is greater than 2.
    if num > 2:
        prime_factors.append(num)

    return prime_factors

print(', '.join([str(x) for x in get_prime_factors(315)]))

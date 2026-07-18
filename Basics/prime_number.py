"""
program: prime number checker
author: G. sai maitra
description: checks whether a given number is a prime number.
"""
n = int(input("Enter a number: "))

is_prime = True
#checks divisibility only upto the square root of n
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        is_prime = False
        break

if is_prime and n > 1:
    print("Yes, it is a Prime number.")
else:
    print("No, it is not a Prime number.")

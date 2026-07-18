"""
program: checking factorial of a number.
author: G.sai maitra
description: checks the factorial of a number.
"""
n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i

print("Factorial =", factorial)

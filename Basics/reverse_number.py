"""
program: reverse a given number
author: G.sai maitra
description: prints the reverse of a number.
"""
n = int(input("Enter a number: "))
reverse = 0
while n > 0:
    digit = n%10
    reverse=reverse*10 + digit
    n = n//10
print("reversed number:", reverse)

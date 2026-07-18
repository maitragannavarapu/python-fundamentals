"""
program: sum of digits
author: G.sai maitra
description: Gives the sum of the digits
"""
n = int(input("Enter a number: "))
sum = 0
while n > 0:
    digit = n%10
    sum = sum + digit
    n = n//10
print(" Sum of the digits:",sum)

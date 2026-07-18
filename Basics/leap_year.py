"""
program: checks leap year or not.
author: G.sai maitra
description: checks if the given year is leap year or not.
"""
n = int(input("Enter a year:"))

if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
    print("It is a leap year.")
else:
    print("It is not a leap year.")

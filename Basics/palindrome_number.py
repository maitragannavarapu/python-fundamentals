""" 
program: palindrome number checker
author: G. sai maitra
description: checks whether a given number is palindrome.
"""
n = int(input("Enter a number: "))
original = n
reverse = 0
while(n>0):
    digit = n%10
    reverse=reverse*10+digit
    n = n//10
if reverse==original:
    print("Yes,it is a palindrome number.")
else:
    print("No,it is not a palindrome number.")

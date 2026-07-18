"""
program: Armstrong Number Checker
Author: G.Sai Maitra
Description: checks whether a given number is a 3 digit is an armstrong number
"""
n = int(input("Enter a number: "))
original=n
armstrong_sum=0
while(n>0):
    digit=n%10
    armstrong_sum=(digit)**3+armstrong_sum
    n=n//10
if armstrong_sum==original:
    print(f"Yes,it is an armstrong number!")
else:
    print(f"No,it is not an armstrong number")

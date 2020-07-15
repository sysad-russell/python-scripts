#! /usr/bin/python3

bar = "*"
print("")
print(bar * 68)
print("This is a simple BASH Compound Interest Calculator.")
print(bar * 68)
print("- sysadRussell")
print("")
print("")
bal = input('How much are we starting with?:  ')           # principal balance
frequency = input('How often is this rate applied?:  ')         # how often rate is applied annualy
rate = input('What is the APR?:  ')          # percent annualy as float
time = input('How many years will this balance collect interest?:  ')           # years accrued
cmpnd_int = float(bal) * ((1 + (float(rate) * .01)/float(frequency)) ** (float(frequency) * float(time)))

total = f"You're total is ${cmpnd_int:.2f} after {time} years."
print(total)

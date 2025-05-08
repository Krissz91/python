#!/usr/bin/python3

import random

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = uppercase.lower()
numbers = "0123456789"
symbols = "()[]{},;:.-_?+*#!@$%^&='<>"

# You can change the booleans if you want it (True/False):
upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
  all += uppercase
if lower:
  all += lowercase
if nums:
  all += numbers
if syms:
  all += symbols

# Here you can change the numbers if you want.
lenght = 20
amount = 10

for x in range(amount):
  password = "".join(random.sample(all, lenght))
  print(password)

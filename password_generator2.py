#!/usr/bin/python3

import random

# Character sets
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = uppercase.lower()
numbers = "0123456789"
symbols = "()[]{},;:.-_?+*#!@$%^&='<>"


# User inputs
try:
    length = int(input("How many characters do you want to use in the password?: "))
    amount = int(input("How many passwords do you want to generate?: "))

    use_upper = input("Do you want to use capital letters? (y/n): ").strip().lower() == "y"
    use_lower = input("Do you want to use lowercase letters? (y/n): ").strip().lower() == "y"
    use_nums = input("Do you want to use numbers? (y/n): ").strip().lower() == "y"
    use_syms = input("Do you want to use symbols? (y/n): ").strip().lower() == "y"
except ValueError:
    print("Invalid input. Please enter only numbers for length and quantity.")
    exit(1)

# We compile the available characters
all_chars = ""
if use_upper:
    all_chars += uppercase
if use_lower:
    all_chars += lowercase
if use_nums:
    all_chars += numbers
if use_syms:
    all_chars += symbols

if not all_chars:
    print("At least one character type must be enabled!")
    exit(1)

# Generate passwords
print("\nGenerated passwords:\n")
for _ in range(amount):
    password = "".join(random.choices(all_chars, k=length))
    print(password)

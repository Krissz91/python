#!/usr/bin/python3

import random

# Character sets
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = uppercase.lower()
numbers = "0123456789"
symbols = "()[]{},;:.-_?+*#!@$%^&='<>"


# User inputs
try:
    length = int(input("Hány karakteres legyen a jelszó? "))
    amount = int(input("Hány jelszót szeretnél generálni? "))

    use_upper = input("Használjon nagybetűket? (i/n): ").strip().lower() == "i"
    use_lower = input("Használjon kisbetűket? (i/n): ").strip().lower() == "i"
    use_nums = input("Használjon számokat? (i/n): ").strip().lower() == "i"
    use_syms = input("Használjon szimbólumokat? (i/n): ").strip().lower() == "i"
except ValueError:
    print("Hibás bemenet. Csak számot adj meg hossz és mennyiség esetén.")
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
    print("Legalább egy karaktertípusnak engedélyezve kell lennie!")
    exit(1)

# Generate passwords
print("\nGenerált jelszavak:\n")
for _ in range(amount):
    password = "".join(random.choices(all_chars, k=length))
    print(password)

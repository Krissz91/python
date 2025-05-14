#!/usr/bin/python3
import os

# Request input
username = input("Add meg a felhasználó nevét: ").strip()
groupname = input("Add meg a csoport nevét: ").strip()

print(f"\nEllenőrzés: {username} felhasználó létezik-e...")

# Does the user exist?
exitcode = os.system(f"id {username} > /dev/null 2>&1")
if exitcode != 0:
    print(f"A(z) {username} felhasználó nem létezik. Létrehozás...")
    os.system(f"useradd {username}")
else:
    print(f"A(z) {username} felhasználó már létezik, kihagyva.")

# Check and create a group
exitcode = os.system(f"getent group {groupname} > /dev/null 2>&1")
if exitcode != 0:
    print(f"A(z) '{groupname}' csoport nem létezik. Létrehozás...")
    os.system(f"groupadd {groupname}")
else:
    print(f"'{groupname}' csoport már létezik, kihagyva.")

# Add user to the specified group
print(f"Felhasználó '{username}' hozzáadása a '{groupname}' csoporthoz...")
os.system(f"usermod -aG {groupname} {username}")

# Create a library
dir_path = f"/opt/{groupname}_dir"
if not os.path.isdir(dir_path):
    print(f"Könyvtár létrehozása: {dir_path}")
    os.mkdir(dir_path)
else:
    print(f"Könyvtár már létezik: {dir_path}, kihagyva.")

# Setting permissions
print("Jogosultságok és tulajdonos beállítása...")
os.system(f"chown :{groupname} {dir_path}")
os.system(f"chmod 770 {dir_path}")

print("\nKész.")

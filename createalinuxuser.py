#!/usr/bin/python3
import os

# Request input
username = input("Enter the user's name: ").strip()
groupname = input("Enter the group's name: ").strip()

print(f"\nChecking: if user {username} exists...")

# Does the user exists?
# With the command > /dev/null it tells the program to direct any output to this so it doesn't come up on the screen and the 2>&1 tells it to direct all errors (2) to the same place you told it to put the output from the first command.
exitcode = os.system(f"id {username} > /dev/null 2>&1")
if exitcode != 0:
    print(f"The user {username} does not exist. Creating...")
    os.system(f"useradd {username}")
else:
    print(f"User {username} already exists, omitted.")

# Check and create a group
exitcode = os.system(f"getent group {groupname} > /dev/null 2>&1")
if exitcode != 0:
    print(f"Group '{groupname}' does not exist. Creating...")
    os.system(f"groupadd {groupname}")
else:
    print(f"Group '{groupname}' already exists, skipped.")

# Add user to the specified group
print(f"Adding user '{username}' to group '{groupname}'...")
os.system(f"usermod -aG {groupname} {username}")

# Create a library
dir_path = f"/opt/{groupname}_dir"
if not os.path.isdir(dir_path):
    print(f"Create a library: {dir_path}")
    os.mkdir(dir_path)
else:
    print(f"Library already exists: {dir_path}, omitted.")

# Setting permissions
print("Setting permissions and owner...")
os.system(f"chown :{groupname} {dir_path}")
os.system(f"chmod 770 {dir_path}")

print("\nReady.")

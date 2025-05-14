#!/usr/bin/python3
import os

userlist = ["alpha", "beta", "gamma"]

print("Adding users to system...")

# Loop to add user from userlist.
for user in userlist:
  exitcode = os.system("id {}".format(user))
  if exitcode != 0:
     print("User {} does not exist. Adding it.".format(user))
     os.system("useradd {}".format(user))
  else:
     print("User already exist. Skipping it.")

# Condition to check if group exists or not, add if not exists.
exitcode = os.system("grep science /etc/group")
if exitcode != 0:
  print("Group science does not exist. Adding it.")
  os.system("groupadd science")
else:
  print("Group already exist, skipping it.")

for user in userlist:
  print("Adding user {} in the science group".format(user))
  os.system("usermod -G science {}".format(user))

print("Adding Directory")

if os.path.isdir("/opt/science_dir"):
  print("Directory already exist, skipping it.")
else:
  os.mkdir("/opt/science_dir")

print("Assigning permission and ownership to the directory.")
os.system("chown :science /opt/science_dir")

os.system("chmod 770 /opt/science_dir")

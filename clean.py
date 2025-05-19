#!/usr/bin/python3

import os
import shutil
import psutil
import time
import platform

# -------- CONFIG --------
TEMP_DIRS = [
    "/tmp",
    os.path.expanduser("~/.cache"),
    os.path.expanduser("~/.pip/cache"),
]
FILE_EXTENSIONS_TO_CLEAN = [".log", ".tmp", ".bak"]
DISK_CLEAN_PATH = "/"  # This directory is being monitored for disk usage
MEMORY_THRESHOLD_MB = 500  # If the free memory drops below this, it will indicate or restart
AUTO_REBOOT = False  # Set to True if the machine can automatically reboot
# -------------------------

def clean_temp_dirs():
    print("Deletion starts...")
    for dir_path in TEMP_DIRS:
        if os.path.exists(dir_path):
            print(f"Cleaning: {dir_path}")
            for root, dirs, files in os.walk(dir_path):
                for name in files:
                    file_path = os.path.join(root, name)
                    try:
                        if os.path.splitext(file_path)[1] in FILE_EXTENSIONS_TO_CLEAN or "cache" in file_path:
                            os.remove(file_path)
                    except Exception as e:
                        print(f"Couldn't delete: {file_path} ({e})")
    print("Cleaning done.")

def system_status():
    print("\nSystem status:")
    mem = psutil.virtual_memory()
    cpu = psutil.cpu_percent(interval=1)
    disk = psutil.disk_usage(DISK_CLEAN_PATH)

    print(f"CPU usage: {cpu}%")
    print(f"Free memory: {round(mem.available / 1024 / 1024)} MB")
    print(f"Disk usage: {disk.percent}% ({DISK_CLEAN_PATH})")

    if mem.available / 1024 / 1024 < MEMORY_THRESHOLD_MB:
        print(f"Free memory low: ({round(mem.available / 1024 / 1024)} MB)")
        if AUTO_REBOOT:
            print("Restart...")
            time.sleep(2)
            if platform.system() == "Linux":
                os.system("sudo reboot")
            else:
                print("Reboot is only supported on Linux.")
        else:
            print("System restart recommended.")

def main():
    clean_temp_dirs()
    system_status()

if __name__ == "__main__":
    main()

# pip3 install psutil --break-system-packages

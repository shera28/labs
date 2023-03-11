import os

path = "first.txt"

if os.path.exists(path):
    if os.access(path, os.F_OK):
        os.remove(path)
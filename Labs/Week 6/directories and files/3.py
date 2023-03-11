import os

path = "first.txt"

if os.path.exists(path):
    print(os.path.basename(path))
    print(os.path.dirname(path))
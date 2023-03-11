import os

path = 'text.txt'

print("Exists:", os.access(path, os.F_OK))
print("Exists:", os.access(path, os.R_OK))
print("Exists:", os.access(path, os.W_OK))
print("Exists:", os.access(path, os.X_OK))
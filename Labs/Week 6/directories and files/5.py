import os

path = "first.txt"
list = [1, 2, 3, 4, 5]

for i in list:
    a = open(path, 'first')
    a.write( "\n" + str(i))
    a.close()
a = open(path, 'r')
print(a.read())
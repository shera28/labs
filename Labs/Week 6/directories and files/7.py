import os

a = open("a.txt", 'r')
b = open("b.txt", 'w')
b.write(a.read())
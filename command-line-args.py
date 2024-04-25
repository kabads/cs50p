import sys

try:
    print("Hello", sys.argv[1])
except IndexError:
    print("Too few errors")

if len(sys.argv) < 2:
    print("Too few arguments")
else:
    print("Hello", sys.argv[1])

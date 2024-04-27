import sys
import csv
from tabulate import tabulate
from PIL import Image

def check_file(args):
    if len(args) < 3:
        print('Too few command-line arguments')
        sys.exit(1)
    elif len(args) > 3:
        print('Too many command-line arguments')
        sys.exit(1)
    extension = args[1].split('.')[-1]
    extensions = ['jpeg', 'jpg', 'png']
    if extension not in extensions:
        print("Invalid input")
        sys.exit(1)
    if args[1].split('.')[-1] != args[2].split('.')[-1]:
        print("Input and output have different extensions")
        sys.exit(1)


def open_file(file):
    try:
      with Image.open(file, mode='r', formats=None) as im:
        print("File found")
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

def main():
    check_file(sys.argv)
    open_file(sys.argv[1])

if __name__ == '__main__':
    main()
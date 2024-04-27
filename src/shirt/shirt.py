import sys
import csv
from tabulate import tabulate

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



def main():
    check_file(sys.argv)

if __name__ == '__main__':
    main()
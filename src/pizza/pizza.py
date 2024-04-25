import sys
import csv
from tabulate import tabulate

def check_file(args):
    if len(args) < 2:
        print('Too few command-line arguments')
        sys.exit(1)
    elif len(args) > 2:
        print('Too many command-line arguments')
        sys.exit(1)
    extension = args[1].split('.')[-1]
    if extension != 'csv':
        print("Not a CSV file")
        sys.exit(1)


def open_file(filename):
    try:
        with open(filename) as f:
            lines = csv.DictReader(f)
            print(tabulate(lines, headers="keys", tablefmt="grid"))
    except:
        print('File does not exist')
        sys.exit(1)
        
        
def main():
    check_file(sys.argv)
    print(open_file(sys.argv[1]))
    
if __name__ == '__main__':
    main()
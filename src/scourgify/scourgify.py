import csv
from tabulate import tabulate
import sys


def check_file(args):
    if len(args) < 3:
        print('Too few command-line arguments')
        sys.exit(1)
    elif len(args) > 3:
        print('Too many command-line arguments')
        sys.exit(1)
    extension = args[1].split('.')[-1]
    if extension != 'csv':
        print("Not a CSV file")
        sys.exit(1)


def open_file(filename, output_file='output.csv'):
    students = []
    try:
        with open(filename) as f:
            reader = csv.DictReader(f)
            data = list(reader)
            # Need to split the names here
            for row in data:
                # Get the first element from a split of the whole name
                # Then remove the last character which is a comma
                last_name = row['name'].split(" ")[0][:-1]
                # Get the second element from a split of the whole name
                first_name = row['name'].split(" ")[1]
                # Build up a list of the pupils
                students.append({'first': first_name, 'last': last_name, 'house': row["house"]})
                # print (f"{first_name}: {last_name} : {row['house']}")
            # data_dict = {i: row for i, row in enumerate(data)}

        # print(students)# print(data_dict)
    except:
        print('File does not exist')
        sys.exit(1)
    try:
        with open(output_file, 'w') as f:
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            [ writer.writerow(student) for student in students]
    except:
        print('Could not write to file')
        sys.exit(1)


def main():
    check_file(sys.argv)
    open_file(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
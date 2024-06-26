import sys


def check_file(sys_argv):
    if len(sys.argv) < 2:
        print('Too few command-line arguments')
        sys.exit(1)
    elif len(sys.argv) > 2:
        print('Too many command-line arguments')
        sys.exit(1)
    extension = sys.argv[1].split('.')[-1]
    if extension != 'py':
        print("Not a Python file")
        sys.exit(1)


def open_file(filename):
    count = 0
    try:
        with open(filename) as f:
            lines = f.readlines()
        for line in lines:
            # print(f"line: {line}")
            if not (line.lstrip().startswith("#") or line.strip() == ""):
                count += 1
            # print(f"count: {count}")
        return count
    except:
        print('File does not exist')
        sys.exit(1)


def main():
    check_file(sys.argv)
    print(open_file(sys.argv[1]))


if __name__ == '__main__':
    main()
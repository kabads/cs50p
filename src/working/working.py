import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    first_search = re.compile(r'\d.?[A|P]')
    results = first_search.finditer(s)
    for match in results:
        print(match.group())


if __name__ == "__main__":
    main()


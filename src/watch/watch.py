import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

    search = re.compile(r"(http(s)?://(www.)?youtube\.com/embed/[a-zA-Z0-9_-]+)")
    match = search.search(s)
    if match:
        return match.group(1)
    else:
        return None


if __name__ == "__main__":
    main()
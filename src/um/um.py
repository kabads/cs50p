import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # A regular expression pattern to find the term um, <space>um<space>, um<period>, um<comma>, um<question mark>, um<exclamation mark>
    pattern = re.compile(r"(\b[uU]m\b[\.,;?!]?)")
    matches = pattern.findall(s)
    if matches:

        return len(matches)
    else:
        return 0




if __name__ == "__main__":
    main()
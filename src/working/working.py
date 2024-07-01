import re
import sys


def main():
    print(convert(input("Hours: ")))


def process_time(match, pattern):
    final_time = ""
    data = pattern.search(match)
    matches = list(data.groups())
    # print(f"matches: {matches}")

    if len(matches[0]) == 1:
        matches[0] = "0" + matches[0]
    # Is it AM? 
    if matches[2] == "A":
        # Is it midnight? 
        if matches[0] == "12":
            matches[0] = "00"
    if matches[2] == "P":
        if matches[0] != "12":
            matches[0] = str(int(matches[0]) + 12)
    final_time = final_time + matches[0] + ":" + matches[1]
    for time in matches:
        if time == '':
            append = "00"
            final_time = final_time + append

    # print(f"Final time {final_time}")
    return final_time


def convert(s):
    # print(f"Converting '{s}'")
    final_string = ""
    pattern = re.compile(r'(\d?\d:?\d?\d?\s?[A|P])M\sto\s(\d?\d:?\d?\d?\s?[A|P])M')
    try: # Check the input - does it match 
        validate_match = pattern.search(s)
        if validate_match == None:
            raise ValueError()
    except re.error as e:        # Raise a ValueError
        raise ValueError()
    
    matches = pattern.findall(s) 

    # pattern = re.compile(r'([0-1]?[1-9]:?[1-9][1-9])?\s?(A|P)')
    pattern = re.compile(r'(\d?\d):?(\d?\d?)\s?([A|P])')
    for match in matches:

        start_time = process_time(str(match[0]), pattern)
        end_time = process_time(str(match[1]), pattern)

        return f"{start_time} to {end_time}"


 

if __name__ == "__main__":
    main()
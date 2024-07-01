import re
import sys


def main():
    # print(convert(input("Hours: ")))
    # print(20 * "-")
    # print(convert("09:00 AM to 05:00 PM"))
    # print(20 * "-")
    # print(convert("9 AM to 5 PM"))
    # print(20 * "-")
    # print(convert("12 AM to 5 PM"))
    # print(20 * "-")
    print(20 * "-")
    print(convert("9:00 AM to 5:00 PM"))
    print(20 * "-")
    print(convert("09:00 AM to 05:00 PM"))
    print(20 * "-")
    print(convert("10:00 AM to 5:00 PM"))


def process_time(match, pattern):
    data = pattern.search(match)
    print(f"Data: {list(data.groups())}")
    # print(f"len of data: {len(data.groups())}")
    # print(list(data.groups()))
    # print(len(data.groups()))
    for time in list(data.groups()):
        if time[0][0] == "0":
            # Delete the first zero
            time = time[-1]
        print(f"Process time returns time {time}")
        return time

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

    # Search match for just the numbers that aren't zero
    # and the AM or PM part.  


    # pattern = re.compile(r'([0-1]?[1-9]:?[1-9][1-9])?\s?(A|P)')
    pattern = re.compile(r'(\d?\d):?(\d?\d?)\s?([A|P])')
    for match in matches:

        start_time = process_time(str(match[0]), pattern)
        end_time = process_time(str(match[1]), pattern)


        find_time = re.compile(r'(\d?\d):?(\d?\d)?\s?([A|P])')
        # print(find_time.search(start_time).groups())
        # print(f"From '{start_time}' to '{end_time}'")
        # Do we have a dobule digit? 
        # Find a space in the match and remove it
 
        if len(start_time) == 2:
            # Is it AM?
            if start_time[-1] == "A":
                final_string = final_string + "0" + start_time[0] + ":00"
            # Is it PM?
            elif start_time[-1] == "P":
                final_string = final_string + start_time[0:2] + ":00"
        elif len(start_time) == 3:
            # Is it AM?

            if start_time[-1] == "A":
                if start_time[:-1] == "12":
                    final_string = final_string + "00:00"
                else:
                    final_string = final_string + start_time[:-1] + ":00"
            # Is it PM?
            elif start_time[-1] == "P":
                final_string = start_time[:-1] + ":00"

        final_string = final_string + " to "
        # Do we have a dobule digit?
        if len(end_time) == 2:
            # Is it AM?
            if end_time[-1] == "A":
                final_string = final_string + "0" + end_time[0] + ":00"
            # Is it PM?
            elif end_time[-1] == "P":
                time = str(int(end_time[:-1])+12)
                final_string = final_string  + time  + ":00"
        elif len(end_time) == 3:
            # Is it AM?
            if end_time[-1] == "A":
                final_string = final_string + end_time[0] + ":00"
            # Is it PM?
            elif end_time[-1] == "P":
                time = str(int(end_time[:-1])+12)
                final_string = final_string + "1" + time  + ":00"
        return final_string

if __name__ == "__main__":
    main()


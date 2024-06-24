import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    final_string = ""
    pattern = re.compile(r'(\d?\d\s?[A|P])M\sto\s(\d?\d\s?[A|P])M')
    try: # Check the input - does it match 
        validate_match = pattern.search(s)
        if validate_match == None:
            raise ValueError()
    except re.error as e:        # Raise a ValueError
        raise ValueError()
    
    
    matches = pattern.findall(s) 
    for match in matches:
        start_time = match[0].replace(" ", "")
        end_time = match[1].replace(" ", "")
        print(f"From '{start_time}' to '{end_time}'")
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


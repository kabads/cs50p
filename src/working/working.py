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
        print(f"From '{match[0]}' to '{match[1]}'")
        # Do we have a dobule digit? 


        if len(match[0]) == 2:
            # Is it AM?
            if match[0][-1] == "A":
                final_string = final_string + "0" + match[0][0] + ":00"
            # Is it PM?
            elif match[0][-1] == "P":
                final_string = final_string + match[0][0:2] + ":00"
        elif len(match[0]) == 3:
            # Is it AM?

            if match[0][-1] == "A":
                if match[0][:-1] == "12":
                    final_string = final_string + "00:00"
                else:
                    final_string = final_string + match[0][:-1] + ":00"
            # Is it PM?
            elif match[0][-1] == "P":
                final_string = match[0][:-1] + ":00"

        final_string = final_string + " to "
        # Do we have a dobule digit?
        if len(match[1]) == 2:
            # Is it AM?
            if match[1][-1] == "A":
                final_string = final_string + "0" + match[1][0] + ":00"
            # Is it PM?
            elif match[1][-1] == "P":
                time = str(int(match[1][:-1])+12)
                final_string = final_string  + time  + ":00"
        elif len(match[1]) == 3:
            # Is it AM?
            if match[1][-1] == "A":
                final_string = final_string + match[1][0] + ":00"
            # Is it PM?
            elif match[1][-1] == "P":
                time = str(int(match[1][:-1])+12)
                final_string = final_string + "1" + time  + ":00"
        return final_string

if __name__ == "__main__":
    main()


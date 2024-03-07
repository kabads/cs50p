
def get_variable():
    return(input("camelCase: "))


def find_upper_position(camel_case):
    upper_chars = []
    for letter in range(len(camel_case)):
        if camel_case[letter].isupper():
            upper_chars.append(letter)
    if upper_chars != []:
        return upper_chars
    else:
        return None


def insert_char(pos, char, string):
    return string[:pos] + char + string[pos:]


def switch_to_camel(position_list, var_name):
    new_var = var_name.lower()
    print(position_list)
    # We need a count because we inserted characters
    count = 0
    for i in position_list:
        print(f"i: {i}\t new_var[i] {new_var[i+count]}")
        new_var = insert_char(i + count, '_', new_var)
        count += 1
    return new_var


def main():
    variable_name = get_variable()
    capital_position_list = find_upper_position(variable_name)
    if capital_position_list != None:
        print(switch_to_camel(capital_position_list, variable_name))
    else:
        print(variable_name)


if __name__ == '__main__':
    main()

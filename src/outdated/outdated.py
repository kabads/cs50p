from datetime import date
import sys

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

list_date = []


while True:
    input_date = input("Date: ").capitalize().strip()
    if '/' in input_date:
        list_date = input_date.split('/')
        if list_date[0].isdigit() == False:
            continue
        if int(list_date[1]) > 31:
            continue
        if int(list_date[0]) > 12:
            continue
        break
    elif [month for month in months if month in input_date]:
        list_date = input_date.split(' ')
        if list_date[1][-1] != ',':
            continue
        if list_date[1][:-1].isdigit() == False:
            continue
        if int(list_date[1][:-1]) > 31:
            continue
        # Need to work out the month from the text
        month = int(months.index(list_date[0]) + 1)
        list_date[0] = month
        list_date[1] = list_date[1][:-1]
        list_date[2] = list_date[2]
        break
    else:
        continue


if len(list_date) != 3:
    print("Invalid date")
    sys.exit()

try:
    month, day, year = map(int, list_date)
    input_date = date(year, month, day)
    print(f"{str(input_date).strip('')}")
except ValueError:
    print("Invalid date")
    sys.exit()
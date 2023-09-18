from datetime import datetime, date
import re, inflect
import sys


def main():
    birth = input("Date of Birth: ")
    if format(birth):
        print(f"{calculate_difference(birth)} minutes")
    else:
        sys.exit("Invalid date")

def format(birth):
    if matches := re.search(r"^[0-2]?[0-9]{1}[0-9]{1}[0-9]{1}-(0[1-9]{1}|1[0-2])-(3[0-1]{1}|[0-2]{1}[0-9]{1}|0[1-9]{1})", birth):
        return True
    else:
        return False

def calculate_difference(birth):
    #today = datetime.now()
    #today = today.replace(hour=0, minute=0, second=0, microsecond=0)
    today = date.today()
    today_date = today.strftime("%Y-%m-%d")
    today_date = datetime.strptime(today_date, "%Y-%m-%d")
    birth_date = datetime.strptime(birth, "%Y-%m-%d")
    time_difference = round((today_date - birth_date).total_seconds() / 60)
    return word_to_number(time_difference)

def word_to_number(number):
    p = inflect.engine()
    word_form = p.number_to_words(number, andword="")
    return word_form.capitalize()

if __name__ == "__main__":
    main()
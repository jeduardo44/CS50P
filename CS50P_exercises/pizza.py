import sys
import csv
from tabulate import tabulate

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

try:
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a csv file")
    else:
        menu = []
        name = sys.argv[1][0:-4]
        name = name.capitalize()
        with open(sys.argv[1], 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                menu.append({name + " Pizza": row[name + " Pizza"], "Small": row["Small"], "Large": row["Large"]})
            print(tabulate(menu, headers='keys', tablefmt='grid'))
except FileNotFoundError:
    sys.exit("File does not exist")

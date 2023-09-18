import sys
import csv

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    if not sys.argv[1].endswith(".csv"):
        sys.exit("File to read is not a csv file")
    else:
        list_of_names_houses = []
        with open(sys.argv[1], 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                list_of_names_houses.append({"name": row["name"], "house": row["house"]})
except FileNotFoundError:
    sys.exit("Could not read " + sys.argv[1])
else:
    if not sys.argv[2].endswith(".csv"):
        sys.exit("File to write is not a csv file")
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in list_of_names_houses:
            names=student['name'].split(",")
            for i in range(len(names)):
                names[i]=names[i].lstrip()
            writer.writerow({"first": names[1], "last":names[0], "house": student["house"]})
            names.clear()
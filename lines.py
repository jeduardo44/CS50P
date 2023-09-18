import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

try:
    if (sys.argv[1][-3:] != ".py"):
        sys.exit("Not a python file")
    else:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
except FileNotFoundError:
    sys.exit("File does not exist")
else:
    count = 0
    for line in lines:
        line=line.lstrip()
        if line.startswith("#"):
            pass
        elif (line==""):
            pass
        else:
            count=count+1
print(count)



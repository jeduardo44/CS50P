import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if "to" not in s:
        raise ValueError()

    s = s.strip()
    if s == "12:00 AM to 12:00 PM":
        return "00:00 to 12:00"

    matches = re.search(
        r"^(1[0-2]|12|[1-9]\:?(?:[0-5][0-9])?)\s(A|P){1}M{1}\sto\s(1[0-2]|12|[1-9]\:?(?:[0-5][0-9])?)\s(A|P){1}M{1}$",
        s,
    )

    if matches:
        hours_1 = matches.group(1)
        hours_2 = matches.group(3)
        format_1 = matches.group(2)
        format_2 = matches.group(4)

        if ":" in hours_1:
            colon_1 = True
        else:
            colon_1 = False
        if ":" in hours_2:
            colon_2 = True
        else:
            colon_2 = False

        if colon_1:
            just_hours_1 = hours_1.split(":")[0]
            minutes_1 = hours_1.split(":")[1]

            if format_1 == "P":
                if just_hours_1 == "12":
                    just_hours_1 = "12"
                else:
                    just_hours_1 = int(just_hours_1) + 12
            else:
                if just_hours_1 == "12":
                    just_hours_1 = "00"
                if int(just_hours_1) < 10 and int(just_hours_1) != 0:
                    just_hours_1 = "0" + just_hours_1

            a = just_hours_1

        else:
            minutes_1 = "00"
            if format_1 == "P":
                if hours_1 == "12":
                    hours_1 = "12"
                else:
                    hours_1 = int(hours_1) + 12
            else:
                if hours_1 == "12":
                    hours_1 = "00"
                if int(hours_1) < 10 and int(hours_1) != 0:
                    hours_1 = "0" + hours_1

            a = hours_1

        if colon_2:
            just_hours_2 = hours_2.split(":")[0]
            minutes_2 = hours_2.split(":")[1]

            if format_2 == "P":
                if just_hours_2 == "12":
                    just_hours_2 = "12"
                else:
                    just_hours_2 = int(just_hours_2) + 12
            else:
                if just_hours_2 == "12":
                    just_hours_2 = "00"
                if int(just_hours_2) < 10 and int(just_hours_2) != 0:
                    just_hours_2 = "0" + just_hours_2

            b = just_hours_2

        else:
            minutes_2 = "00"

            if format_2 == "P":
                if hours_2 == "12":
                    hours_2 = "12"
                else:
                    hours_2 = int(hours_2) + 12
            else:
                if hours_2 == "12":
                    hours_2 = "00"
                if int(hours_2) < 10 and int(hours_2) != 0:
                    hours_2 = "0" + hours_2
            b = hours_2
        return str(a) + ":" + str(minutes_1) + " to " + str(b) + ":" + str(minutes_2)

    else:
        raise ValueError()


if __name__ == "__main__":
    main()

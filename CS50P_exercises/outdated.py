def main():
    while True:
        try:
            date = input("Date: ")
        except EOFError:
            pass
        else:
            result = treat_date(date)
            if result=="Bad Format":
                pass
            else:
                print (result)
                break

def treat_date(date):
    list_of_months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
    }

    ls_date1=date.split("/")

    if len(ls_date1)==3:
        try:
            month = int(ls_date1[0])
            day = int(ls_date1[1])
            year = int(ls_date1[2])
        except ValueError:
            return "Bad Format"
        else:
            pass

        if (1 <= day <= 31) and (1 <= month <= 12):
            return f"{year:04}-{month:02}-{day:02}"
        else:
            return "Bad Format"

    else:
        ls_date2=date.split()

        if len(ls_date2)==3:
            if "," in ls_date2[1]:
                ls_date2[1]=ls_date2[1].strip(",")
            else: return "Bad Format"

            try:
                day = int(ls_date2[1])
                year = int(ls_date2[2])
            except ValueError:
                return "Bad Format"
            else:

                if (ls_date2[0] in list_of_months) and (1 <= day <= 31):
                    month =  list_of_months[ls_date2[0]]
                    return f"{year:04}-{month:02}-{day:02}"
                else:
                    return "Bad Format"

        else:
            return "Bad Format"



    return result

main()

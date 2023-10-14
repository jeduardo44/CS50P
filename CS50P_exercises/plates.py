def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

#to initialize, we have a true statement with n=1 and the valid chars to validate after

    n=1
    s=s.upper()
    valid_alchars='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    valid_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    valid_nums='0123456789'
    first_number=0

    while True:
#check if the length of string is between 6 and 2
        if len(s)>6 or len(s)<2:
            return False

#check if the first two chars are letters
        for i in range(2):
            if s[i] not in valid_chars :
                return False

#check for some punctation, spaces or other marks than alphanumerics chars
        for i in range(len(s)):
            if s[i] not in valid_alchars:
                return False

#check if the first number encountered is 0. If is 0, n turns 0. Record also the position of first number.
        for j in s:
            if j in valid_nums:
                if j=='0':
                    return False

        for p in range(len(s)):
            if s[p] in valid_nums:
                first_number=p
                break

#Check if there is letter after the first number
        if first_number !=0:
            for x in range(first_number+1, len(s)):
                if s[x] in valid_chars:
                    return False
        return True

if __name__ == "__main__":
    main()

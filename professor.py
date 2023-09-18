import random

def main():
    score = 0
    level= get_level()
    count=0
    while (count < 10):


        errors = 0
        a = (generate_integer(level))
        b = (generate_integer(level))
        result = int(input(str(a) + " + " + str(b) + " = "))

        while (errors < 3):
            if (result == (a+b)):
                score = score+1
                break
            elif(result != (a+b)):
                print("EEE")
                errors = errors+1
                if (errors <3):
                    result = int(input(str(a) + " + " + str(b) + " = "))
                elif (errors==3):
                    correct_result=a+b
                    print(f"{str(a)} + {str(b)} = {str(correct_result)}")
                    break
        count = count +1;
        score=score+1;
    print ("Score:", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if 0 < level <= 3:
                break
            else:
                pass
    return level


def generate_integer(level):

    if 0 < level <= 3:
        if (level ==1):
            number_generated = random.randint(0, 9)
        elif (level==2):
            number_generated = random.randint(10, 99)
        else:
            number_generated = random.randint(100, 999)
        return number_generated
    else:
         raise ValueError

if __name__ == "__main__":
    main()
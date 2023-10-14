import sys
import json
import requests
import re


def main():
    if len(sys.argv) != 2:
        sys.exit(
            "Invalid App name. You should choose between: Validator, Calculator, Trivia"
        )
    if (
        sys.argv[1] == "Validator"
        or sys.argv[1] == "Calculator"
        or sys.argv[1] == "Trivia"
    ):
        match sys.argv[1]:
            case "Validator":
                number = input("Introduce your number (with +351 extension or not): ")
                if validate_number(number):
                    print("This is a valid portuguese number")
                else:
                    print("Not a valid portuguese number")

            case "Calculator":
                while True:
                    print("Options:\n")
                    print("Enter 'add' for addition")
                    print("Enter 'subtract' for subtraction")
                    print("Enter 'multiply' for multiplication")
                    print("Enter 'divide' for division")
                    print("Enter 'square' for number square")
                    print("Enter 'quit' to end the program")
                    print()

                    operation = input("Choose an option from the above: ")

                    if operation == "quit":
                        break

                    elif operation in ["add", "subtract", "multiply", "divide"]:
                        num1 = input("Enter first number: ")
                        num2 = input("Enter second number:")
                        print()
                        print(f"Result: {calculator(num1, num2, operation)}\n")
                    elif operation == "square":
                        num1 = input("Enter number: \n")
                        print()
                        print(f"Result: {calculator(num1,0, operation)}")
                    else:
                        print("Not a valid operator")

            case "Trivia":
                try:
                    response = requests.get("https://opentdb.com/api.php?amount=1")
                    response_data = response.json()

                except (requests.RequestException, json.JSONDecodeError):
                    sys.exit("Failed to fetch a question.")

                else:
                    if "results" in response_data and len(response_data["results"]) > 0:
                        print()
                        print(response_data["results"][0]["question"])
                        print()
                        print("Choose one from the next ones:\n")
                        print(response_data["results"][0]["correct_answer"])
                        for i in range(
                            len(response_data["results"][0]["incorrect_answers"])
                        ):
                            print(response_data["results"][0]["incorrect_answers"][i])
                        print()
                        answer = input("What's your answer? ")

                        while True:
                            if (
                                answer != response_data["results"][0]["correct_answer"]
                                and answer
                                not in response_data["results"][0]["incorrect_answers"]
                            ):
                                print()
                                print(response_data["results"][0]["question"])
                                print()
                                print("Choose one from the next ones: \n")
                                print(response_data["results"][0]["correct_answer"])
                                for i in range(3):
                                    print(
                                        response_data["results"][0][
                                            "incorrect_answers"
                                        ][i]
                                    )
                                print()
                                answer = input("What's your answer? ")
                            else:
                                print(
                                    trivia(
                                        response_data["results"][0]["correct_answer"],
                                        answer,
                                    )
                                )
                                print()
                                break

                    else:
                        print("No question found in the response.")
    else:
        print(
            "Invalid App name. You should choose between: Validator, Calculator, Trivia"
        )


def validate_number(number):
    if len(number[-9 : len(number)]) != 9:
        raise ValueError("A portuguese number should have 9 digits after extension")
    matches = re.search(r"^(?:\+351)?9[1236][0-9]{7}$", str(number))
    if matches:
        return True
    else:
        return False


def calculator(num1, num2, operation):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Invalid number"
    else:

        def add(x, y):
            return x + y

        def subtract(x, y):
            return x - y

        def multiply(x, y):
            return x * y

        def divide(x, y):
            if y == 0:
                return False
            return x / y

        def square(x):
            return x**2

        if operation == "add":
            return add(num1, num2)
        elif operation == "subtract":
            return subtract(num1, num2)
        elif operation == "multiply":
            return multiply(num1, num2)
        elif operation == "divide":
            if divide(num1, num2) == False:
                return "Cannot divide by zero"
            else:
                return divide(num1, num2)
        elif operation == "square":
            return square(num1)

        else:
            return "Invalid input"


def trivia(corr_answer, answer):
    if type(corr_answer) != str or type(answer) != str:
        raise ValueError
    if answer == corr_answer:
        feedback = "That's the right answer, congrats"
        return feedback
    else:
        feedback = f"Sorry, but the right answer is {corr_answer}"
        return feedback


if __name__ == "__main__":
    main()

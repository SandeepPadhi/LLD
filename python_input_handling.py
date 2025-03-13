def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_valid_age():
    while True:
        try:
            age = int(input("Enter your age (1-120): "))
            if 1 <= age <= 120:
                return age
            else:
                print("Age must be between 1 and 120.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    # 1. Basic Input with Type Conversion
    a = int(input("Enter an integer: "))
    b = float(input("Enter a float: "))
    print(f"Sum: {a + b}")

    # 2. Error Handling with try-except
    try:
        a = int(input("Enter an integer: "))
        b = int(input("Enter another integer: "))
        print(f"Sum: {a + b}")
    except ValueError:
        print("Invalid input. Please enter integers only.")

    # 3. Input Validation with Loops
    a = get_integer_input("Enter an integer: ")
    b = get_integer_input("Enter another integer: ")
    print(f"Sum: {a + b}")

    # 4. Handling Multiple Input Values (Splitting)
    input_string = input("Enter two numbers separated by a space: ")
    try:
        a, b = map(int, input_string.split())
        print(f"Sum: {a + b}")
    except ValueError:
        print("Invalid input. Please enter two numbers separated by a space.")

    # 5. Handling Different Delimiters
    input_string = input("Enter numbers separated by commas: ")
    try:
        numbers = [int(x) for x in input_string.split(",")]
        print(f"Sum: {sum(numbers)}")
    except ValueError:
        print("Invalid input. Please enter numbers separated by commas.")

    # 6. Input Validation with Specific Ranges
    age = get_valid_age()
    print(f"Your age is: {age}")

    # 7. Handling File Input
    try:
        with open("input.txt", "r") as file:
            numbers = [int(line.strip()) for line in file]
            print(f"Sum: {sum(numbers)}")
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Invalid data in file.")

if __name__ == "__main__":
    main()
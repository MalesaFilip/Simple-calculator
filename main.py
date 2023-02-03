def add(n1, n2):
    return n1 + n2


def subtraction(n1, n2):
    return n1 - n2


def multiplication(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


def power(n1, n2):
    return n1 ** n2


print("Select your operation.")
print("1. Add")
print("2. Subtraction.")
print("3. Multiplication.")
print("4. Division.")
print("5. Power.")


while True:
    choice = input("Enter your choice(1/2/3/4/5): ")
    if choice in ("1", "2", "3", "4", "5"):
        result = 0
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Wrong input. Please enter a number.")
            continue
        if choice == "1":
            result = add(num1, num2)
            print(num1, "+", num2, "=", result)
        elif choice == "2":
            result = subtraction(num1, num2)
            print(num1, "-", num2, "=", result)
        elif choice == "3":
            result = multiplication(num1, num2)
            print(num1, "*", num2, "=", result)
        elif choice == "4":
            result = division(num1, num2)
            print(num1, "/", num2, "=", result)
        elif choice == "5":
            result = power(num1, num2)
            print(num1, "**", num2, "=", result)
        continue_with_result = input(f"Do you want to do calculation with {result}?(yes/no): ")
        if continue_with_result == "yes":
            new_result = 0
            while True:
                choice = input("Enter your choice(1/2/3/4/5): ")
                if choice in ("1", "2", "3", "4", "5"):
                    try:
                        num2 = float(input("Enter second number: "))
                    except ValueError:
                        print("Wrong input. Please enter a number.")
                        continue
                    if choice == "1":
                        new_result = add(result, num2)
                        print(result, "+", num2, "=", new_result)
                    elif choice == "2":
                        new_result = subtraction(result, num2)
                        print(result, "-", num2, "=", new_result)
                    elif choice == "3":
                        new_result = multiplication(result, num2)
                        print(result, "*", num2, "=", new_result)
                    elif choice == "4":
                        new_result = division(result, num2)
                        print(result, "/", num2, "=", new_result)
                    elif choice == "5":
                        new_result = power(result, num2)
                        print(result, "**", num2, "=", new_result)
                    continue_with_result = input(f"Do you want to do calculation with {new_result}?(yes/no): ")
                    result = new_result
                    if continue_with_result == "no":
                        break
                else:
                    print("Invalid input.")
            next_calculation = input("Do you want to do next calculation?(yes/no): ")
            if next_calculation == "no":
                break
        else:
            next_calculation = input("Do you want to do next calculation?(yes/no): ")
            if next_calculation == "no":
                break
    else:
        print("Invalid input.")
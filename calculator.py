import math

def calculator():
    print("\n--- Extended Basic Calculator ---")

    while True:
        print("\nAvailable operations:")
        print(" 1 → Addition")
        print(" 2 → Subtraction")
        print(" 3 → Multiplication")
        print(" 4 → Division")
        print(" 5 → Power")
        print(" 6 → Modulus")
        print(" 7 → Square root")
        print(" 8 → Percentage (x% of y)")
        print(" 9 → Exit")

        try:
            choice = input("\nChoose operation (1-9): ").strip()

            if choice == "9":
                print("Exiting calculator. Goodbye!")
                break

            elif choice == "7":  
                num = float(input("Enter number: "))
                if num < 0:
                    print("Error: Cannot calculate square root of a negative number.")
                    continue
                result = math.sqrt(num)
                print(f"√{num} = {result}")

            elif choice == "8":
                x = float(input("Enter percentage (x): "))
                y = float(input("Enter number (y): "))
                result = (x * y) / 100
                print(f"{x}% of {y} = {result}")

            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    result = num1 + num2
                elif choice == "2":
                    result = num1 - num2
                elif choice == "3":
                    result = num1 * num2
                elif choice == "4":
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        print("Error: Division by zero not allowed.")
                        continue
                elif choice == "5":
                    result = num1 ** num2
                elif choice == "6":
                    if num2 != 0:
                        result = int(num1) % int(num2)
                    else:
                        print("Error: Modulus by zero not allowed.")
                        continue
                else:
                    print("Invalid choice! Please enter 1–9.")
                    continue

                print(f"Result: {result}")

        except ValueError:
            print("Invalid input, please enter numbers.")


if __name__ == "__main__":
    calculator()

def menu():
    print("\nSelect an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not possible"
    
def main():
    while True:
        menu()
        choice = input("Enter the choice number or 'q' to quit: ")

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("\nEnter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == '1':
                    result = add(num1, num2)
                    print(f"\nResult: {num1} + {num2} = {result}")
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"\nResult: {num1} - {num2} = {result}")
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"\nResult: {num1} * {num2} = {result}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"\nResult: {num1} / {num2} = {result}")

            except ValueError:
                print("Invalid input. Please enter numeric values.")
        
        elif choice.lower() == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    main()

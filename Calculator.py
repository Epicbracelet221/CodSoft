class Calculator:
    def __init__(self):
        self.history = []

    def add(self, num1, num2):
        result = num1 + num2
        self.history.append(f"{num1} + {num2} = {result}")
        return result

    def subtract(self, num1, num2):
        result = num1 - num2
        self.history.append(f"{num1} - {num2} = {result}")
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.history.append(f"{num1} * {num2} = {result}")
        return result

    def divide(self, num1, num2):
        if num2 == 0:
            return "Error: Division by zero"
        result = num1 / num2
        self.history.append(f"{num1} / {num2} = {result}")
        return result

    def view_history(self):
        if not self.history:
            print("No history available.")
        else:
            print("Calculation History:")
            for calc in self.history:
                print(calc)

    def clear_history(self):
        self.history = []
        print("History cleared.")

def main():
    calculator = Calculator()
    while True:
        print("\n===== Calculator =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. View History")
        print("6. Clear History")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == '1':
                print("Result:", calculator.add(num1, num2))
            elif choice == '2':
                print("Result:", calculator.subtract(num1, num2))
            elif choice == '3':
                print("Result:", calculator.multiply(num1, num2))
            elif choice == '4':
                print("Result:", calculator.divide(num1, num2))
        elif choice == '5':
            calculator.view_history()
        elif choice == '6':
            calculator.clear_history()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

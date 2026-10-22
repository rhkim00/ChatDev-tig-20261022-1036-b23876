import json
import os
import matplotlib.pyplot as plt

class FinanceTracker:
    def __init__(self, filename):
        self.filename = filename
        self.data = {}

    def read_file(self):
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
            return self.data
        except FileNotFoundError:
            print("File Not Exists")
            return None
        except json.JSONDecodeError:
            print("Invalid JSON format")
            return None

    def write_file(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    def add_income(self, category, amount):
        if category in self.data:
            self.data[category]['income'] += amount
        else:
            self.data[category] = {'income': amount, 'expenses': 0}

    def add_expense(self, category, amount):
        if category in self.data:
            self.data[category]['expenses'] += amount
        else:
            self.data[category] = {'income': 0, 'expenses': amount}

    def get_balance(self, category):
        if category in self.data:
            return self.data[category]['income'] - self.data[category]['expenses']
        else:
            return 0

    def plot_spending(self):
        categories = list(self.data.keys())
        incomes = [self.data[category]['income'] for category in categories]
        expenses = [self.data[category]['expenses'] for category in categories]
        plt.bar(categories, incomes, label='Income')
        plt.bar(categories, expenses, bottom=incomes, label='Expenses')
        plt.xlabel('Category')
        plt.ylabel('Amount')
        plt.title('Spending Habits')
        plt.legend()
        plt.show()


def main():
    filename = input("Enter filename: ")
    tracker = FinanceTracker(filename)

    while True:
        print("\nOptions:")
        print("1. Read file")
        print("2. Add income")
        print("3. Add expense")
        print("4. Get balance")
        print("5. Plot spending")
        print("6. Quit")

        option = input("Choose an option: ")

        if option == '1':
            data = tracker.read_file()
            if data:
                print(json.dumps(data, indent=4))
        elif option == '2':
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            tracker.add_income(category, amount)
            tracker.write_file()
        elif option == '3':
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            tracker.add_expense(category, amount)
            tracker.write_file()
        elif option == '4':
            category = input("Enter category: ")
            print(tracker.get_balance(category))
        elif option == '5':
            tracker.plot_spending()
        elif option == '6':
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()

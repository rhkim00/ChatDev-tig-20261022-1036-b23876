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
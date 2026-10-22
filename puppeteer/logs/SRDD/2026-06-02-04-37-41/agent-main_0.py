import json
import os
import datetime
import csv

class ShoppingOrganizer:
    def __init__(self, filename):
        self.filename = filename
        self.categories = {}

    def read_file(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File {self.filename} not found.")
            return None
        except json.JSONDecodeError:
            print(f"Failed to parse JSON in file {self.filename}.")
            return None

    def create_file(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump({'items': [], 'categories': {}}, file)
            return True
        except Exception as e:
            print(f"Failed to create file {self.filename}: {str(e)}")
            return False

    def add_item(self, item):
        data = self.read_file()
        if data is None:
            data = {}
        if 'items' not in data:
            data['items'] = []
        if 'categories' not in data:
            data['categories'] = {}
        data['items'].append(item)
        if item['category'] not in data['categories']:
            data['categories'][item['category']] = []
        data['categories'][item['category']].append(item)
        self.write_file(data)

    def remove_item(self, item_name):
        data = self.read_file()
        if data is None:
            return
        if 'items' in data:
            data['items'] = [item for item in data['items'] if item['name'] != item_name]
            self.write_file(data)

    def update_item(self, item_name, quantity=None, note=None):
        data = self.read_file()
        if data is None:
            return
        if 'items' in data:
            for item in data['items']:
                if item['name'] == item_name:
                    if quantity is not None:
                        item['quantity'] = quantity
                    if note is not None:
                        item['note'] = note
                    self.write_file(data)
                    return

    def write_file(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file)

    def display_items(self):
        data = self.read_file()
        if data is None:
            return
        if 'items' in data:
            for item in data['items']:
                print(f"Name: {item['name']}, Quantity: {item['quantity']}, Note: {item['note']}, Category: {item['category']}")

    def display_categories(self):
        data = self.read_file()
        if data is None:
            return
        if 'categories' in data:
            for category, items in data['categories'].items():
                print(f"Category: {category}")
                for item in items:
                    print(f"  - Name: {item['name']}, Quantity: {item['quantity']}, Note: {item['note']}")

    def add_category(self, category):
        data = self.read_file()
        if data is None:
            data = {}
        if 'categories' not in data:
            data['categories'] = {}
        if category not in data['categories']:
            data['categories'][category] = []
        self.write_file(data)

    def remove_category(self, category):
        data = self.read_file()
        if data is None:
            return
        if 'categories' in data:
            if category in data['categories']:
                del data['categories'][category]
                self.write_file(data)

    def generate_shopping_list(self):
        data = self.read_file()
        if data is None:
            return
        if 'items' in data:
            shopping_list = []
            for item in data['items']:
                if item['quantity'] == '0' or item['quantity'] == '':
                    shopping_list.append(item)
            return shopping_list

    def export_data(self):
        data = self.read_file()
        if data is None:
            return
        with open('shopping_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Quantity', 'Note', 'Category'])
            for item in data['items']:
                writer.writerow([item['name'], item['quantity'], item['note'], item['category']])

    def set_reminder(self, item_name, reminder_date):
        data = self.read_file()
        if data is None:
            return
        if 'items' in data:
            for item in data['items']:
                if item['name'] == item_name:
                    item['reminder_date'] = reminder_date
                    self.write_file(data)
                    return

    def check_reminders(self):
        data = self.read_file()
        if data is None:
            return
        if 'items' in data:
            today = datetime.date.today()
            for item in data['items']:
                if 'reminder_date' in item and item['reminder_date'] == today.strftime('%Y-%m-%d'):
                    print(f"Reminder: {item['name']}")

def main():
    filename = input("Enter the filename to read: ")
    organizer = ShoppingOrganizer(filename)

    if not os.path.exists(filename):
        print("File does not exist. Creating a new file...")
        organizer.create_file()

    while True:
        print("\nShopping Organizer Menu:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Update item")
        print("4. Display items")
        print("5. Display categories")
        print("6. Add category")
        print("7. Remove category")
        print("8. Generate shopping list")
        print("9. Export data")
        print("10. Set reminder")
        print("11. Check reminders")
        print("12. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter item name: ")
            quantity = input("Enter item quantity: ")
            note = input("Enter item note: ")
            category = input("Enter item category: ")
            organizer.add_item({'name': name, 'quantity': quantity, 'note': note, 'category': category})
        elif choice == '2':
            name = input("Enter item name to remove: ")
            organizer.remove_item(name)
        elif choice == '3':
            name = input("Enter item name to update: ")
            quantity = input("Enter new quantity (press enter to skip): ")
            note = input("Enter new note (press enter to skip): ")
            category = input("Enter new category (press enter to skip): ")
            if quantity == '':
                quantity = None
            if note == '':
                note = None
            if category == '':
                category = None
            organizer.update_item(name, quantity, note, category)
        elif choice == '4':
            organizer.display_items()
        elif choice == '5':
            organizer.display_categories()
        elif choice == '6':
            category = input("Enter category name: ")
            organizer.add_category(category)
        elif choice == '7':
            category = input("Enter category name to remove: ")
            organizer.remove_category(category)
        elif choice == '8':
            shopping_list = organizer.generate_shopping_list()
            if shopping_list:
                print("Shopping list:")
                for item in shopping_list:
                    print(f"Name: {item['name']}, Quantity: {item['quantity']}, Note: {item['note']}")
            else:
                print("No items to purchase.")
        elif choice == '9':
            organizer.export_data()
            print("Data exported to shopping_data.csv")
        elif choice == '10':
            name = input("Enter item name to set reminder: ")
            reminder_date = input("Enter reminder date (YYYY-MM-DD): ")
            organizer.set_reminder(name, reminder_date)
        elif choice == '11':
            organizer.check_reminders()
        elif choice == '12':
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
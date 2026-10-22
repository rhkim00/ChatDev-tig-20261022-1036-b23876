import json
import os

class ZooSimulator:
    def __init__(self, data_file):
        self.data_file = data_file

    def read_file(self):
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File {self.data_file} not found.")
            return None
        except json.JSONDecodeError:
            print(f"Failed to parse JSON in file {self.data_file}.")
            return None
        except Exception as e:
            print(f"Error processing file {self.data_file}: {str(e)}")
            return None

    def write_file(self, data):
        try:
            with open(self.data_file, 'w') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Failed to write to file {self.data_file}: {str(e)}")

    def create_default_data(self):
        return {
            "enclosures": [],
            "animals": [],
            "staff": [],
            "visitors": 0,
            "animal_happiness": 0,
            "visitor_happiness": 0
        }

def main():
    data_file = input("Enter the filename you want to read: ")
    simulator = ZooSimulator(data_file)

    if not os.path.exists(data_file):
        data = simulator.create_default_data()
        simulator.write_file(data)
        print(f"Created default data in file {data_file}")
    else:
        data = simulator.read_file()
        if data is not None:
            print(f"Loaded data from file {data_file}: {data}")

if __name__ == "__main__":
    main()

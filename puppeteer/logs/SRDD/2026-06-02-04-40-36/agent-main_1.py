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
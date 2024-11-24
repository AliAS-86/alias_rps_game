"""Placeholder"""
import json
import os

class JsonHandler:
    """This class can be called at any script to load json files into memory and provide 
    access to the key, values without the need to access the raw json file, this make
    the code logic resistant to any JSON format/structure changes"""
    def __init__(self):
        self.json_file_path = None
        self.data = {}
        self.load_json_data()

    def file_locator(self):
        """Placeholder"""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.json_file_path = os.path.join(current_dir, "./data/" + "validation_data.json")
        print(self.json_file_path)
        return self.json_file_path


    def load_json_data(self):
        """Instance method to load the JSON file into memory"""
        json_file_path = self.file_locator()
        try:
            with open(json_file_path, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            print(f"Specified JSON file {json_file_path} not found. Using default")
            self.data = {}

        except json.JSONDecodeError:
            print(f"Error decoding the JSON file {json_file_path}. Using default")
            self.data = {}

    def get_validation_data(self, key):
        """Placeholder"""
        value = self.data.get("validation_data", {}).get(key)
        return value
    
    def reload_file(self):
        """Placeholder"""
        self.load_json_data()


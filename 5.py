python
```
# 39.7 Contact Book Using JSON
import json

class PhoneDirectory:
    def __init__(self, file_name="phone_data2.json"):
        self.file_name = file_name
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number

    def search_contact(self, name):
        print(f"Search '{name}': {self.contacts.get(name, 'Not Found')}")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact Removed: {name}")
        else:
            print(f"Contact '{name}' not found.")

    def show_contacts(self):
        print("\n--- Phone Directory ---")
        for name, number in self.contacts.items():
            print(f"{name:<20}: {number}")

    def save_contacts(self):
        with open(self.file_name, "w") as file:
            json.dump(self.contacts, file, indent=4)
        print("Contacts saved successfully.")

    def load_contacts(self):
        try:
            with open(self.file_name, "r") as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            print(f"File '{self.file_name}' not found. Creating a new directory.")

directory = PhoneDirectory()
directory.load_contacts()

directory.add_contact("Aarav Shah", "9876543210")
directory.add_contact("Diya Patel", "9812345670")
directory.add_contact("Krish Mehta", "9723456780")
directory.add_contact("Riya Joshi", "9634567890")
directory.add_contact("Dev Shah", "9545678901")

directory.show_contacts()
directory.search_contact("Aarav Shah")
directory.remove_contact("Rohan Patel")
directory.save_contacts()
```
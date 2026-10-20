python
```
# 32.7 Phone Book
phonebook = {}

# (a) Add 5 contacts
phonebook["Aarav"] = "9876501234"
phonebook["Diya"] = "9876502345"
phonebook["Krish"] = "9876503456"
phonebook["Anaya"] = "9876504567"
phonebook["Rohan"] = "9876505678"

# (b) Search by name
search_name = "Krish"
print(f"Search '{search_name}': {phonebook.get(search_name, 'Not Found')}")

# (c) Update a number
phonebook["Aarav"] = "9898989898"
print(f"Updated Aarav's number: {phonebook['Aarav']}")

# (d) Delete a contact
deleted = phonebook.pop("Anaya", None)
print(f"Deleted contact 'Anaya': {deleted}")

# (e) Display all contacts sorted by name
print("\nContacts sorted by name:")
for person in sorted(phonebook.keys()):
    print(f"  {person:<10} : {phonebook[person]}")
```
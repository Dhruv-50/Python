
python
```
# 18.6 Default Parameter Function

def show_details(name, city="Mumbai", program="BCA"):
    print(f"Name: {name:<10} | City: {city:<10} | Course: {program}")

print("(a) Calling with all 3 arguments:")
show_details("Amit Patel", "Surat", "BBA")

print("\n(b) Calling with only name:")
show_details("Priya")

print("\n(c) Calling with name and city:")
show_details("Rahul", "Jaipur")
```
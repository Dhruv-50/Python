python
```
# 29.6 Inventory Management System

inventory = {}

def add_product(product, qty):
    inventory[product] = inventory.get(product, 0) + qty

def delete_product(product):
    if product in inventory:
        del inventory[product]
    else:
        print(f"Product '{product}' not found.")

def change_quantity(product, qty):
    if product in inventory:
        inventory[product] = qty
    else:
        print(f"Product '{product}' does not exist.")

def show_inventory():
    print(f"\n{'Product':<15} | {'Stock':<10}")
    print("-" * 28)
    for product, qty in inventory.items():
        print(f"{product:<15} | {qty:<10}")

def check_low_stock():
    low_items = {
        product: qty
        for product, qty in inventory.items()
        if qty < 6
    }
    print(f"\nLow Stock Items (<6): {low_items if low_items else 'None'}")

# Sample Operations
add_product("Notebooks", 20)
add_product("Pens", 5)
add_product("Erasers", 3)
add_product("Markers", 14)

show_inventory()
check_low_stock()

change_quantity("Pens", 10)
delete_product("Erasers")

print("\n--- Updated Inventory ---")
show_inventory()
```
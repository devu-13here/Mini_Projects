menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80,
}

print("Welcome to PYTHON RESTAURANT!")
print("Here is our menu:")
for item, price in menu.items():
    print(f"{item}: Rs {price}")

order_total = 0
ordering = True

while ordering:
    item_1 = input("Enter the name of the item you want to order: ").capitalize()

    if item_1 in menu:
        order_total += menu[item_1]
        print(f"Your item {item_1} has been added to your order.")
    else:
        print("Sorry, we don't have that item. Please order something from the menu.")

    another_order = input("Do you want to add another item? (Yes/No): ").capitalize()
    if another_order == "No":
        ordering = False

print(f"The total amount to pay is Rs {order_total}. Thank you for dining with us!")

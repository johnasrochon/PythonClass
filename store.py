from catalog import catalog # import your catalog list

# ------------------------------
# Shopping Cart Program
# ------------------------------

# Store inventory (5 items)
store = [
    {"id": 1, "title": "Shoes", "price": 49.99},
    {"id": 2, "title": "Hat", "price": 19.99},
    {"id": 3, "title": "Backpack", "price": 59.99},
    {"id": 4, "title": "Socks", "price": 5.99},
    {"id": 5, "title": "Jacket", "price": 89.99}
]

# Shopping cart (starts empty)
cart = []


# ------------------------------
# FUNCTIONS
# ------------------------------
def view_store():
    print("\nSTORE ITEMS")
    print("| ID | Item        | Price  |")
    print("|----|-------------|--------|")
    for item in store:
        print(f'| {item["id"]} | {item["title"].ljust(11)} | ${item["price"]:.2f}')
    print()


def add_to_cart():
    view_store()
    choice = int(input("Enter the ID of the item to add: "))
    
    for item in store:
        if item["id"] == choice:
            cart.append(item)
            print(f"{item['title']} added to cart!")
            return
    print("Item not found.")


def delete_from_cart():
    view_cart()
    if not cart:
        return
    
    choice = int(input("Enter ID of item to delete: "))
    
    for item in cart:
        if item["id"] == choice:
            cart.remove(item)
            print(f"{item['title']} removed from cart!")
            return
    print("Item not in cart.")


def search_item():
    word = input("Enter item name to search: ").lower()
    
    found = False
    for item in store:
        if word in item["title"].lower():
            print(f"FOUND → {item['title']} - ${item['price']:.2f}")
            found = True
    
    if not found:
        print("Item not found in store.")


def view_cart():
    print("\nYOUR CART:")
    if not cart:
        print("Your cart is empty!\n")
        return
    
    print("| ID | Item        | Price  |")
    print("|----|-------------|--------|")
    
    total = 0
    for item in cart:
        print(f'| {item["id"]} | {item["title"].ljust(11)} | ${item["price"]:.2f}')
        total += item["price"]

    print(f"\nTOTAL PRICE: ${total:.2f}\n")


def clear_cart():
    cart.clear()
    print("Shopping cart cleared!")


# ------------------------------
# MAIN MENU LOOP
# ------------------------------
while True:
    print("\n--- SHOPPING CART MENU ---")
    print("1. View Store Items")
    print("2. Add Item to Cart")
    print("3. Delete Item from Cart")
    print("4. Search for Item")
    print("5. View Shopping Cart")
    print("6. Clear Cart")
    print("7. Exit")

    option = input("Choose an option (1-7): ")

    if option == "1":
        view_store()
    elif option == "2":
        add_to_cart()
    elif option == "3":
        delete_from_cart()
    elif option == "4":
        search_item()
    elif option == "5":
        view_cart()
    elif option == "6":
        clear_cart()
    elif option == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")

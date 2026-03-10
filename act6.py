class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        item = Item(name, price)
        self.items.append(item)
        print(name, "added to cart.")

    def remove_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                print(name, "removed from cart.")
                return
        print("Item not found.")

    def show_cart(self):
        if not self.items:
            print("Cart is empty.")
        else:
            print("Your Cart:")
            total = 0
            for item in self.items:
                print(item.name, "- ₱", item.price)
                total += item.price
            print("Total: ₱", total)

    def checkout(self):
        if not self.items:
            print("Cart is empty.")
        else:
            total = sum(item.price for item in self.items)
            print("Total amount to pay: ₱", total)
            print("Checkout successful. Thank you!")
            self.items.clear()


shopping = Cart()

while True:
    print("\n--- Shopping Cart ---")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    option = input("Select option: ")

    if option == "1":
        name = input("Product name: ")
        price = float(input("Product price: "))
        shopping.add_item(name, price)

    elif option == "2":
        name = input("Product name to remove: ")
        shopping.remove_item(name)

    elif option == "3":
        shopping.show_cart()

    elif option == "4":
        shopping.checkout()

    elif option == "5":
        print("Program ended.")
        break

    else:
        print("Invalid option.")
class Item:
    def __init__(self, item_id, name, price, quantity):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} (ID: {self.item_id}): ${self.price} x {self.quantity}"

class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def create_item(self, item_id, name, price, quantity):
        if item_id in self.cart:
            print(f"Item with ID {item_id} already exists.")
        else:
            self.cart[item_id] = Item(item_id, name, price, quantity)
            print(f"Added {name} to the cart.")

    def read_item(self, item_id):
        if item_id in self.cart:
            return str(self.cart[item_id])
        else:
            return f"Item with ID {item_id} not found in the cart."

    def update_item(self, item_id, name=None, price=None, quantity=None):
        if item_id in self.cart:
            item = self.cart[item_id]
            if name is not None:
                item.name = name
            if price is not None:
                item.price = price
            if quantity is not None:
                item.quantity = quantity
            print(f"Updated item with ID {item_id}.")
        else:
            print(f"Item with ID {item_id} not found in the cart.")

    def delete_item(self, item_id):
        if item_id in self.cart:
            del self.cart[item_id]
            print(f"Deleted item with ID {item_id}.")
        else:
            print(f"Item with ID {item_id} not found in the cart.")

    def list_items(self):
        if not self.cart:
            print("The cart is empty.")
        else:
            for item_id, item in self.cart.items():
                print(self.read_item(item_id))

# Demonstration
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.create_item(1, "Apple", 0.5, 10)
    cart.create_item(2, "Banana", 0.2, 5)
    print(cart.read_item(1))
    cart.update_item(1, price=0.55)
    cart.update_item(2, quantity=8)
    cart.list_items()
    cart.delete_item(1)
    cart.list_items()

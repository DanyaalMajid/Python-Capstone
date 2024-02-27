class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price} - {self.quantity} in stock"
    

class Inventory():
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def total_value(self):
        return sum([product.price * product.quantity for product in self.products])

    def __str__(self):
        return "\n".join([str(product) for product in self.products])

    def restock_product(self, product, quantity):
        product.quantity += quantity

    def sell_product(self, product, quantity):
        if product.quantity < quantity:
            print("Not enough stock")
        else:
            product.quantity -= quantity

    def search_product(self, name):
        return [product for product in self.products if product.name == name][0]

    def search_product_by_price(self, price):
        return [product for product in self.products if product.price == price]

    def search_product_by_quantity(self, quantity):
        return [product for product in self.products if product.quantity == quantity]
    

def main():
    inventory = Inventory()
    inventory.add_product(Product("Apple", 1, 100))
    inventory.add_product(Product("Banana", 2, 150))
    inventory.add_product(Product("Orange", 3, 200))
    inventory.add_product(Product("Pear", 4, 250))
    inventory.add_product(Product("Peach", 5, 300))
    print(inventory)
    print(inventory.total_value())
    inventory.restock_product(inventory.search_product("Apple"), 100)
    print(inventory)
    inventory.sell_product(inventory.search_product("Apple"), 50)
    print(inventory)
    print(inventory.total_value())
    print(inventory.search_product_by_price(2))
    print(inventory.search_product_by_quantity(300))

if __name__ == "__main__":
    main()
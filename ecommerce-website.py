class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.purchases = []

    def purchase(self, inventory, product):
        inventory_dict = inventory.inventory
        if product in inventory_dict:
            if inventory_dict[product] > 0:
                self.purchases.append(product)
                inventory_dict[product] -= 1
            else:
                print("We are out of stock")
        else:
            print("Item not found")

    def print_purchases(self):
        print("The customer has purchased;")
        for item in self.purchases:
            print(item.name)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product, quantity):
        if product not in self.inventory:
            self.inventory[product] = quantity
        else:
            self.inventory[product] += quantity

    def print_inventory(self):
        for key, value in self.inventory.items():
            print(key.name + " : " + str(value))
        print()


c1 = Customer('Birr', 'farming@farms.com')

bottle = Product('Water Bottle', 20)
plate = Product('Plate (20)', 10)

inventory = Inventory()
inventory.add_product(bottle, 100)
inventory.add_product(plate, 200)

inventory.print_inventory()
c1.purchase(inventory, bottle)
c1.purchase(inventory, plate)
inventory.print_inventory()
c1.print_purchases()

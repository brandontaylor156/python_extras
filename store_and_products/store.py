from product import Product

class Store:
    def __init__(self, name, products = {}):
        self.name = name
        self.products = products

    def add_product(self, new_product):
        self.products[new_product.id] = new_product
        return self

    def sell_product(self, id):
        deletedProd = self.products.pop(id)
        deletedProd.print_info()
        print("\n")
        return self

    def inflation(self, percent_increase):
        for products in self.products.values():
            products.update_price(percent_increase, True)
        return self

    def clearance(self, percent_discount):
        for products in self.products.values():
            products.update_price(percent_discount, False)
        return self

    def display_store_catalogue(self):
        for products in self.products.values():
            products.print_info()
        print('\n')
        return self

newProduct1 = Product("Toothpaste", 10, "Hygiene")
newProduct2 = Product("Cereal", 5, "Breakfast Foods")
newProduct3 = Product("Apple", 1, "Fruits")
newStore= Store("Vons")

newStore.add_product(newProduct1).add_product(newProduct2).add_product(newProduct3)
newStore.display_store_catalogue()
newStore.sell_product(newProduct1.id)
newStore.inflation(.08).display_store_catalogue()
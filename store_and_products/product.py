class Product:
    currentID = 0

    @classmethod
    def createNewID(cls):
        cls.currentID += 1

    def __init__(self, name, price, category):
        self. name = name
        self.price = price
        self.category = category
        Product.createNewID()
        self.id = Product.currentID

    def update_price(self, percent_change, is_increased):
        if is_increased is True:
            self.price += (self.price * percent_change)
        else:
            self.price -= (self.price * percent_change)
        return self

    def print_info(self):
        print(f"Product Name: {self.name}   ID: {self.id}   Price: {'${:,.2f}'.format(self.price)}   Category: {self.category}")

    
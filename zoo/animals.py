class Animal:
    def __init__(self, name):
        self.name = name

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)
        
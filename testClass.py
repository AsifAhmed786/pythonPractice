class Car:
    def __init__(self,make,model,price):
        self.make = make
        self.model = model
        self.price = price

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getPrice(self):
        return self.price

    def setPrice(self,price1):
        self.price = price1
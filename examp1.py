class Car():
    def __init__(self,make,model,price):
        self.make = make
        self.model = model
        self.price = price

    def getCarDetails(self):
        print(self.make,self.model,self.price)
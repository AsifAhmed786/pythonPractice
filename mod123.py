def function1():
    print("this is modules function")

def function2():
    print("this is function 2")


class Car:
    def __init__(self,make,model,price):
        self.make = make
        self.model = model
        self.price = price

    def getCarDetails(self):
        print(f"Car make is {self.make} Car model is {self.model} Car price is {self.price}")
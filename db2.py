# var1 = 123
# var2 = "new"
# var3 = ["hello1","hello2","hello3"]
# var4 = "asif","imran","wajahat"
# var5 = {"new1","new2","new3"}

# def func1():
#     print("this is function1 of module")

class Car:
    def __init__(self,make,model,price):
        self.make = make
        self.model = model
        self.price = price

    def getDetailOfCar(self):
        print(self.make,self.model,self.price)
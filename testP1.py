import mod123 as mod1

mod1.function1()

car1 = mod1.Car("Suzuki","Yaris",2000000)
car1.getCarDetails()


def getPizzaDetail(flavor, price, *toppings):
    print(flavor, price, toppings)


getPizzaDetail("Tikka",1000,"onions","olives","ketchup")


print(5//2)

a = 5;
b = 10
c = a+b
str1 = "hello"+ str(c)
print(str1)
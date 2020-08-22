# def func1():
#     print("hello")

# def func2(var1,var2):
#     print(var1,var2);

# def funct3(flavor,price,*toppings):
#     print(flavor,price,toppings)

# # funct3("Chicken Tikka",2000,"olives","onion","cheese")

# def func4():
#     return 234


# print(func4())


# import db2 as db

# print(db.var1,db.var2,db.var3,db.var4,db.var5)
# db.func1()

# car1 = db.Car("Suzuki","Swift",1800000)
# car1.getDetailOfCar()


# with open("asif.txt","a") as file1:
#     file1.write("hello1\n")
#     file1.write("hello2\n")
#     file1.write("hello3\n")


# with open("asif.txt") as file1:
#     print(file1.read())
    

# with open("asif.txt","w+") as file1:
#     file1.write("asif1\n")
#     file1.write("asif2\n")
#     file1.write("asif3\n")
#     file1.seek(0)
#     print(file1.read())



# import csv as csv1

# with open("asif.csv","w",newline="") as file1:
#     out = csv1.writer(file1,delimiter=",")
#     out.writerow(["Name","Father Name","Age","Education"])
#     out.writerow(["Asif","Ahmed","40","ICMA"])
#     out.writerow(["Imran","Jamal","40","Intermediate"])

# with open("asif.csv") as file1:
#     cont = csv1.reader(file1)
#     for con in cont:
#         print(con)


# import json as js1

# list1 = ["Bcom","intermediate","matriculation"]
# with open("asif.json","w") as file1:
#     js1.dump(list1,file1)


# with open("asif.json") as file1:
#     cont = js1.load(file1)
#     print(cont)
#     for c in cont:
#         print(c)


# list1 = ["Book1","Book2","Book3","Book4"]

# try:
#     print(list1[1])
# except Exception as err:
#     print(f"error generated {err}")
# else:
#     print("this is else")
# finally:
#     print("this is finally")


import pandas as pd1

import pandas as pd

dict1 = {"Name":["Asif","Imran","Hanif Turk"],"Father Name":["Ahmed","Jamal","Turk"],"Education":["ICMA","Intermediate","MA Economics"]}
print(pd.DataFrame(dict1))
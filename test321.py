list1 = ["Pakistan","China","srilanka","trukey"]
print(list1)


# for abc in list1:
#     print(abc)

for i in range(4):
    print(list1[i])

print(list1[0:1])


cities = "karachi","islamabad","lahore"

print(type(cities))

# del cities[0]
print()


a = dict()
a["name"] = ["Asif","Ahmed","Imran","New"]
a["fname"] = ["Ahmed","Abdul Sattar","Jamal","Newf"]


print(a)


import pandas as p1

dataframe = p1.DataFrame(a)
print(dataframe)


def fun1():
    print("this is function 1")
    return 1


af = fun1()
print(af)


def func2(par1,par2):
    print(par1,par2)


func2("Asif","Ahmed")


def func3(par1,par2,*par3):
    print(par1,par2,par3)

func3("asif","ahmed","icmaqualified","withjob","eligible bachlor")


import testmod1 as t1

t1.fun1();



class Student:
    def __init__(self,name,fname,age):
        self.name = name
        self.fname = fname
        self.age = age

    def getAll(self):
        print(self.name,self.fname,self.age)

std1 = Student("Asif","Ahmed",40)
std1.getAll()

try:
    print(list1[1])
except Exception as e:
    print(e," this is exception")
else:
    print("else")
finally:
    print("this is finally")

with open("test123.txt","w") as file:
    file.write("hello")
    file.write("hello")
    file.write("hello")
    file.write("hello")
    
with open ("test123.txt","r") as file:
    print(file.read())

import csv as csv1
with open("test123.csv","w",newline="") as file1:
    out = csv1.writer(file1,delimiter=",")
    out.writerow(["Name","Father Name","Age"])
    out.writerow(["Asif","Ahmed",40])
    out.writerow(["Imran","Jamal",40])
    out.writerow(["Hanif","Turk",40])


with open("test123.csv") as file1:
    read1 = csv1.reader(file1)
    for con in read1:
        print(con)

import json as js1
with open("test321.json","w") as file1:
    js1.dump(a,file1)

with open("test321.json","r") as file1:
    cont = js1.load(file1)
    print(cont)


    
    


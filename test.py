# a = {"key1":"asif", "Key2":"ahmed"}
# a.update({"key1":"new"})
# print(a)
# list1 = [{"Age":25,"qua":"bcom"},{"first":"asif","last":"ahmed"}]
# print(list1[0].items())

# dic1 = {"asif":{"fname":"Ahmed","age":40,"qual":"ACMA"},"Imran":{"fname":"Jamal","age":41,"qual":"inter"}}
# # print(dic1.items())

# print(dic1["asif"].items())


global count
count = 5

def funct():
    global count
    count = 10
    print(count)

funct()
print(count)



abc = "asif"
print(f"my brother name is {abc}")
print("my brother name is {}".format(abc))

abc = True

while abc:
    print("hello")
    exit()

import mod as module1

print(module1.add(2,4))
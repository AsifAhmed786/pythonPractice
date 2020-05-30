abc = 10;
print(abc)
print(type(abc//5))


fname="Asif"
lname = "Ahmed"
print(f"My name is {fname} {lname}")
print("My name is {}{}".format(fname,lname))

print("asif",end="*")
print("ahmed",end="*")
print("imran",end="*")

print("asif","ahmed",sep="%")

asif = "asif"
Asif = "asif"
print(asif)
print(Asif)

if asif==Asif:
    print("true")
else:
    print("false")

cities = ["Karachi","Islamabad","Rawalpindi","Quetta"]
print(len(cities))
if "Karachi" in cities:
    print("true")
else:
    print("false")

if "Karach" in cities or "Islamabad" in cities:
    print("true")
# else:
    print("false")

cities.append("hello")
print(cities)

print(cities.count("Karachi"))
cities.insert(0,"new hello")
print(cities)
cities.sort(reverse=False)
print(cities)
cities.pop()




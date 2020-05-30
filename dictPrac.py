dic = dict()
print(dic)
dic["hello"] = "new world"
print(dic["hello"])


qual = {"Asif":"ICMA","Imran":"Intermediate","Hanif":"M.com"}
# print(qual[0])


for a in qual:
    print(a)

print(qual)
qual.popitem()
print(qual)

print(qual.values())
qual.update({"Asif":"ACMA"})
print(qual)



diclist = {"Asif":["Ahmed","ACMA","Karachi"],"Imran":["Jamal","Inter","Lahore"],"Hanif":["Turk","M.com","Islamabad"]}
diclist2 = {"Asif":{"Qualification":"ACMA","City":"Karachi"},"Imran":{"Qualification":"Intermediate","City":"Lahore"}}


if "Asif" in diclist:
    print("true")
else:
    print("false")

# del diclist["Asif"]

print(diclist["Asif"][1])


print(diclist2["Asif"]["City"])

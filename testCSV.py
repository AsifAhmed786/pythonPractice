import csv as csv1

with open("test1.csv") as file1:
    content_of_file = csv1.reader(file1)
    print(type(content_of_file))
    for content in content_of_file:
        print(type(content))


with open("test2.csv","w",newline="") as file1:
    out = csv1.writer(file1,delimiter=",")
    out.writerow(["Name1","Father1","Age1"])
    out.writerow(["Asif1","Ahmed1","40a"])
    out.writerow(["Imran1","Jamal1","41a"])
    out.writerow(["Wajahat1","Ameen1","42a"])


with open("test2.csv","a",newline="") as file1:
    out = csv1.writer(file1,delimiter=",")
    out.writerow(["aAsif1","aAhmed1","a40a"])
    out.writerow(["aImran1","aJamal1","a41a"])
    out.writerow(["aWajahat1","aAmeen1","a42a"])
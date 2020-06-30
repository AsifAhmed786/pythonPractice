# with open("hello123.txt","a") as file1:
#     file1.write("hello1\n")
#     file1.write("hello2\n")
#     file1.write("hello3\n")
#     file1.write("hello4\n")

# with open("hello123.txt","r") as file1:
#     print(file1.read())

import csv as csv1

with open("io123.csv","w",newline="") as file1:
    out = csv1.writer(file1,delimiter=",")
    out.writerow(["Name","FatherName","Education"])
    out.writerow(["Asif","Ahmed","ICMA"])
    out.writerow(["Asif1","Ahmed1","ICMA1"])
    out.writerow(["Asif2","Ahmed2","ICMA2"])

with open("io123.csv","r") as file1:
    read1 = csv1.reader(file1)
    for line in read1:
        print(line)
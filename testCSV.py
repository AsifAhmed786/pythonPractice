import csv as csv1

with open("test1.csv") as file1:
    content_file = csv1.reader(file1)
    for content in content_file:
        print(content)


with open("test2.csv","w",newline="") as file1:
    out = csv1.writer(file1,delimiter=",")
    out.writerow(['Name', 'FatherName', '40'])
    out.writerow(['11Asif123', 'Ahmed', '40'])
    out.writerow(['11Asif123', 'Ahmed', '40'])

with open("test2.csv") as file1:
    content_file = csv1.reader(file1)
    for content in content_file:
        print(content)
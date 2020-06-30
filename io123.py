with open("hello123.txt","a") as file1:
    file1.write("hello1\n")
    file1.write("hello2\n")
    file1.write("hello3\n")
    file1.write("hello4\n")

with open("hello123.txt","r") as file1:
    print(file1.read())
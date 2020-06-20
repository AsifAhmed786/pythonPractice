with open("test21.txt","r") as file1:
    print(file1.read())

with open("test21.txt","w") as file1:
    file1.write("no thats not true\n")
    file1.write("no thats not true\n")
    file1.write("no thats not true\n")


with open("test21.txt","a") as file1:
    file1.write("hello1")
    file1.write("hello2")
    file1.write("hello3")

with open("test214.txt","w+") as file1:
    file1.write("hello world\n")
    file1.write("hello world2\n")
    file1.write("hello world3\n")
    file1.seek(0)
    print(file1.read())
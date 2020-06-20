with open("new1.txt","r") as file:
    file_content = file.read()
    print(file_content)


with open("new1.txt","w") as file:
    file.write("what is your name dear\n")
    file.write("what is your name dear1\n")
    file.write("what is your name dear2\n")


with open("new1.txt","a") as file:
    file.write("What is you name append")
    file.write("What is you name append1")
    file.write("What is you name append2")

with open("new2.txt","w+") as file:
    file.write("hellomynewworld")
    file.seek(0);
    print(file.read());
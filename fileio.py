# with open("testnew.txt","w") as file1:
#     file1.write("hello how r u\n")
#     file1.write("hello how r u\n")
#     file1.write("hello how r u\n")
#     file1.write("hello how r u\n")

# with open("testnew.txt","r") as file1:
#     content = file1.read()
#     print(content)


with open("testnew2.txt","w+") as file1:
    file1.write("hello1")
    file1.write("hello2")
    file1.write("hello3")
    file1.write("hello4")
    file1.seek(0)
    content = file1.read()

    print(content) 
class Student:
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def getName(self):
        return self.fname

    def setName(self,newName):
        self.fname = newName

    def getProfile(self):
        print(f"First Name: {self.fname}")
        print(f"Last Name: {self.lname}")
        print("Age: {}".format(self.age))

stud1 = Student("Asif","Ahmed","40")
stud1.getProfile()
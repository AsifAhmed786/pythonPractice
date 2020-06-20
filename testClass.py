class Student:
    def __init__(self,name,fname,rollnumber,age):
        self.name = name
        self.fname = fname
        self.rollnumber = rollnumber
        self.age = age
    
    def getStudentProfile(self):
        print(f"Student name is {self.name}")
        print(f"Student Father name is {self.fname}")
        print(f"Student Father name is {self.rollnumber}")
        print(f"Student age is {self.age}")


# st1 = Student("Asif","Ahmed",1127,40)
# st1.getStudentProfile()
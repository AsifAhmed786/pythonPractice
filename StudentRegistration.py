#practice session
#Student registration program
dic = dict()
# while(True):
#     registerStudent()
count = 0
record = dict()
situation = True
def registerStudent():
        list = []
        list.append(str(input("\n\nPlease enter your name: ")))
        list.append(str(input('Please enter your father name: ')))
        list.append(str(input('Please enter your CNIC: ' )))
        list.append(str(input("Please enter your country: ")))
        list.append(str(input('Please enter your city: ')))
        record[str(count+1)] = list


        print("Record Successfully Saved", end="\n\n")
def deleteStudent():
    print("this is delete function")

def reviewStudent():
    recNo = input("\n\nPlease enter record number:")
    # print(recNo)
    # print(record["recNo"])
    print(record[str(recNo)],end="\n\n")
    # print("\n\n",record)

def fetchRecord():
    for a in dic:
        print(a)

while situation:
    command = input("Please enter your requirement \n 1.Enter new record \n 2.Delete student's record \n 3.Review student's record \n 4.Fetch whole record \n 5.Exit from registration system \n Give your input:")
    if command=="1":
        registerStudent()
    elif command=="2":
        deleteStudent()
    elif command=="3":
        reviewStudent()
    elif command=="5":
        exit()
    else:
        print("You have selected wrong option\n\n")

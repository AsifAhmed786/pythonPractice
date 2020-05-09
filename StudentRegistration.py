1#practice session
#Student registration program

# while(True):
#     registerStudent()
global count
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
        global count
        count = count + 1
        record[str(count)] = list
        print("\nResult is:")
        print("Record Successfully Saved")
        print("*************************", end="\n\n")

def deleteStudent():
    print(end="\n\n")
    recNo = input("\n\nPlease enter record number:")
    temprecNo = str(recNo)
    if temprecNo in record:
        del record[str(recNo)]
        print("Record deleted")
        print("*************************", end="\n\n")
    else:
        print("Record Not Found")
        print("*************************", end="\n\n")
    print(end="\n\n")

def reviewStudent():
    recNo = input("\n\nPlease enter record number:")
    print("Result is:")
    temprecNo = str(recNo)
    if temprecNo in record:
        print(f"Record No: {temprecNo} Details: {record[temprecNo]}")
        print("*************************", end="\n\n")
    else:
        print("Record Not Found")
        print("*************************", end="\n\n")
    # print(recNo)
    # print(record["recNo"])
    # print(record[str(recNo)],end="\n\n")
    # print("\n\n",record)

def fetchRecord():
    print("\n\nResult is:")
    for a in record:
        print(f"Record No: {a} Details: {record[a]}")
    print("*************************", end="\n\n")

print("\n\n")
print("***********************************")
print("***********************************")
print("***********************************")
print("|xxx STUDENT REGISTRATION FORM xxx|")
print("***********************************")
print("***********************************")
print("***********************************")
print("\n\n")


while situation:
    command = input("Please enter your requirement \n 1.Enter new record \n 2.Delete student's record \n 3.Review student's record \n 4.Fetch whole record \n 5.Exit from registration system \n Give your input:")
    if command=="1":
        registerStudent()
    elif command=="2":
        deleteStudent()
    elif command=="3":
        reviewStudent()
    elif command=="4":
        fetchRecord()
    elif command=="5":
        print("\n\nThank you for using student registration system, stay healthy, stay safe")
        exit()
    else:
        print("You have selected wrong option\n\n")

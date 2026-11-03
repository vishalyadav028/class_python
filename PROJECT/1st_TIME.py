print("--------------Student Management System--------------------")

Management = []

def studentdata():
    name = input("Enter The Student Name: ")
    marks = int(input("Enter The Student Marks: "))

    Student = {
        "name": name,
        "marks": marks
    }

    Management.append(Student)

    print("Student Added Successfully!")
    print("-" * 30)

while True:
    studentdata()

    choice = input("Add Another Student? (Yes/No): ")

    if choice.lower() == "no":
        break
    elif choice.lower() == "yes":
        continue


print("\n--- Student Records ---")

for std in Management:
    print("Name:", std["name"])
    print("Marks:",std)

    if std["marks"] >= 33:
        print("Result is Passed")
    else:
        print("Result is Failed")

    print("-" * 30)


def search_student():
    search_name = input("Enter The Student Name to Search: ")

    for std in Management:
        if(std["name"].lower() == search_name.lower()):

            print("Student Found!")
            
            print("Name:", std["name"])
            print("Marks:", std["marks"])
            return
        
    print("Student Not Found!")

def update_student():
    search_name = input("Enter The name to update: ")

    for std in Management:
        if(std["name"].lower() == search_name.lower()):

            new_marks = int(input("Enter New Marks:"))  
            std["marks"] = new_marks    

            print("student Updated Successfull!")
            return 
        print("student not found")

update_student()

print("All Student Data:")

for std in Management:
    ("Name", std(["name"]))
    ("Marks", std(["marks"]))

    if(std["marks"] >= 33):
        print("Result is passed")
    else:
        print("Result is Failed")    

print("-"*30)


print(Management)







print(Management)

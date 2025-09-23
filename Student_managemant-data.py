Student_data = ("Edify the sdudent management data")
Adimin_data = ("godabharath@123","9u38375364","Room 231")

print(f"welcome to the {Student_data}")
print(f"developed by the {Adimin_data}")

students = {}


# Menue

while True:
    print("Select the any options")
    print("1 -- Add student")
    print("2 -- modify student")
    print("3 -- Delete student")
    print("4 -- Exist system")

    choices = input("Slect the options:")
    if choices == "1":
        print("Add the student")
    elif choices == "2":
        print("modify the student")
    elif choices == "3":
        print("Delete the student")
    elif choices == "4":
        print("Exits the system")
        break
    else:
        print("Student's are missmatches")        
        

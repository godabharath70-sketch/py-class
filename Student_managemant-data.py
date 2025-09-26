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
    print("4 -- Listsing students logic")
    print("5 -- Exist system")
    print("System is done")
    print("My system is done")

    choices = input("Slect the options:")
    if choices == "1":
        print("Add the student")
        student_Id = input("Enter the ID:")
        if student_Id in students:
            print("ID is already is exits")
        else:
            name = input("Enter the name:").title()
            scrores = []
            while True:
                score_input = input("Enter the score or type done:")
                if score_input == "done":
                    break
                if score_input.isdigit():
                    scoree = int(score_input)
                    if 0 <= scoree <=100:
                        scrores.append(scoree)
                    else:
                        print("score should be  in the range 0 to 100")
                else:
                    print("Score can be the numbers only") 
                               
            My_skills = set()    
            while True:
                skill_input = input("Enter the skills or type done:")
                if skill_input == "done":
                    break
                My_skills.add(skill_input.title())

            students[student_Id] = {
                    "name":name,
                    "scores":scrores,
                    "skills":My_skills,
              }
            print("Student add succfully")
            print(students)
                                                               
    elif choices == "2":
        print("modify the student")
        student_Id = input("Enter the ID:")
        if student_Id in students:
            new_name = input("Enter the new name:").title()
            students[student_Id]["name"] = new_name
            print("student name is updated")
            if student_Id in students:
                new_scoree = input("Enter the new score:")
                students[student_Id]["scores"] = new_scoree
                print("student score is updated succufully")  
            else:
                print("student score is not updated")    

        else:
            print("Student ID is not found")
        print(students)    

    elif choices == "3":
        print("Delete the student")
        student_Id = input("Enter the ID:")
        if student_Id in students:
            remove = students.pop(student_Id)
            print("student removed succfully:",remove)
        else:
            print("Student ID is not deleted")
        print(students)

    elif choices == "4":
        print("Listing the student")
        if not students:
            print("No student are the avivblie")
        else:
            print("student are listed below")
            for sid, data in students.items():
                name = data["name"]
                scrores = data["scores"]
                avge = sum(scrores)/len(scrores)
                high_score = max(scrores)
                skill_input = data["skills"]
                skills = len(skill_input)
                print("_______*****________")
                print(f"My Student ID:{sid}")
                print(f"My student name:{name}")
                print(f"My student Scores:{scrores}")
                print(f"My srudent Average:{avge}")
                print(f"My Student Hig scoresss:{high_score}")
                print(f"My student skills:{skill_input}")
                print(f"My Student total skills:{skills}")                
                print("_______*****________")

    elif choices == "5":
        print("Exist the system")
    else:
        print("Student's are missmatches")        
        

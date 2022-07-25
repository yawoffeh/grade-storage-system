from time import sleep
from os import system as sys #just to clear the console

options = """
Please Select one option. Enter the numbers attached to them....

    [1]- To add a new student details
    [2]- To search for a students grade
    [3]- To read all the content in the dictionary
    [4]- To update a student grade \n
"""
#---------------------------------------------------------------------------------------------
def update(act):
    file = open("student_details.txt", "w")
    file.write(f"students = {act}")
    file.close()

def add_student(new_dict):
    update(new_dict)
    return ""

def get_student_grade(id, main_dict):
    return main_dict.get(id, "Please the Id does not exist....")

#---------------------------------------------------------------------------------------------
def main():
    print(options)
    lastid = list(all_details.keys())[-1]
    try:
        selection = int(input())
        if selection == 1:
            student_id = int(lastid) + 1
            z = "0" * (3-len(str(student_id)))
            print(f"New Id created ------>> {z}{student_id}")
            res = input("Please enter the 5 grades for the students, please seperate with space \n")
            try:
                grades = list(res.split(" "))
                all_details[f"{z}{student_id}"] = grades
                update(all_details)
                print("Done!")
                main()
            except:
                print("Please enter all the 5 grades")
        elif selection == 2:
            student_id = input("Please the Id of the student: \n")
            try:
                print(f"{student_id} -----> {get_student_grade(student_id, all_details)}")
                main()
            except:
                print(f"The student ID \"{student_id}\" does not exist")
        elif selection == 3:
            print("Getting all grades........")
            for i in all_details.items():
                print(i, end="\n")
        elif selection == 4:
            student_id = input("Please the Id of the student you wish to upgrade the grades : \n")
            try:
                student_grades = all_details[student_id]
                print(f"Student grades--->  {student_grades}\n")
                print()
                print(f"Which grade do you want to upgrade [Grade1, Grade2, Grade3, Grade4, Grade5]: \n")
                grade = input()
                try:
                    grade_pos = int(grade)-1
                    if int(grade) <= len(student_grades):
                        grade_value = student_grades[grade_pos]
                        print(f"previous grade ---> {grade_value}")
                        student_grades.pop(grade_pos)
                    else:
                        pass
                    new_grade = input("Enter the new grade: ")
                    student_grades.insert(grade_pos, new_grade)
                    all_details[student_id] = student_grades
                    update(all_details)
                    print("Done!!")
                except:
                    print("Action Unsucessful")
            except KeyError:
                print(f"The ID \"{student_id}\" does not exist..")
    except ValueError:
        print("Invalid Input....")
        sleep(2)
        main()


if __name__ == "__main__":
    sys("cls")
    student_details = open("student_details.txt", "r")
    all_details = eval(" ".join([x for x in student_details])[10:])
    main()

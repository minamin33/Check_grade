from average import average_grade
class GradeManager:
    def __init__(self):
        self.student = {} #empty dictionary
    def enter_students(self):
        try:
            num_students = int(input("Enter the number of students: "))
            for i in range(num_students):
                while True:
                  student_id = input("Enter the student ID: ")
                  if student_id in self.student:
                      print("Student ID is already there,please enter another one")
                  else:
                    name = input("Enter the student name: ")
                    self.student[student_id] = {"name" : name, "grade": [] }
                    print("Students added successfully!")
                    break
        except:
            print("Invalid input, please add a number")

    def enter_assignments(self):
        try:
            student_id = input("Enter the student ID to add assignments: ")
            if student_id in self.student:
                grades_str = input("Enter " + self.students[student_id]["name"]  + " assignments, space seperated ")
                grades_list = [float(grade) for grade in grades_str.split()]
                self.students[student_id]["grades"] = grades_list
                print("Assignments added successfully!")
        except:
            print("Invalid input, please add grades")
    def find_students_assignments(self):
        name = input("Enter student name to find assignments: ")
        if name in self.student:
            print( name + "assignments: "+ self.student(name))
        else:
            print(name + "not found")
    def find_students_average(self):
        name = input("Enter student name get average score: ")
        if name in self.student:
            avg_score =  average_grade.calculate_avg(self.student(name))
            print(name + " average score is " + avg_score)
    def quit_program(user_input):
        print("Exiting the program")
        exit()



from grade_calculation import GradeCalculation
from average_grade import calculate_avg

if __name__ == "__main__":

    try:
        student_grades = {}
        num_students = int(input("Enter the number of students: ")
        for i in range(num_students):
        name = input("Enter the student name: ")
        grades_str = input("Enter {name} assignments:")  
                
        grades = grades_str.split()
        grades = []
            for grade in grades:
                grades.append(float(grade))

        if name in student_grades:
            avg_grade = calculate_avg(student_grade(name))
            final_grade = GradeCalculation(avg_grade)
            print("The average grade for {name} is : {final_grade}")
        else:
            print("Student {name} is not found" )
            add = input(" Would you like to insert them? (yes/no)")
                if add == "yes":
                    

    except:
        print("Invalid input")
            

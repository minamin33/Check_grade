from grade_calculation import GradeCalculation
from average_grade import calculate_avg

if __name__ == "__main__":

    try:
        student_grades = {}
        num_students = int(input("Enter the number of students: ")
        for i in range(num_students):
        name = input("Enter the student name: ")
        grades_str = float(input("Enter (name) assignments:")  
                
        grades = grade_str.split()
        for i in range (len(grades)):
            grades[i]= float(grades[i])
        search = ("Enter the student name to search: ")

        if name in student_grade:
            avg_grade = calculate_avg(student_grade(name))
            final_grade = GradeCalculation(avg_grade)
            print("The average grade for (name) is : (final_grade)")
        else:
            print("Student (name) is not found" )
            print(" Would you like to insert them?")
            

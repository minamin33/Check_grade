from grade_calculation import GradeCalculation

if __name__ == "__main__":

    try:
        num_work = int(input("How many assignments?"))
        student = input("Student name:")
        grade = input("What is the grade per assignment?")
        student_grades = grade.split()
        for i in range (len(student_grades)):
            student_grades[i]= int(student_grades[i])
            

        
        score = float(input("Enter score:"))
        print(computegrade(score))
    
    except:
        print ("Incorrect input, please try again")
        

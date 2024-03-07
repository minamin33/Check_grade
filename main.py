from grade_calculation import GradeCalculation


if __name__ == "__main__":

    try:
        num_work = int(input("How many assignments?"))
        student = input("Student name:")
        grade = input("What is the grade per assignment?")
        student_grades = grade.split()
        for i in range (len(student_grades)):
            student_grades[i]= float(student_grades[i])
            
        grade_calculator = GradeCalulation()
        

        
        score = float(input("Enter score:"))
        print(computegrade(score))
    
    except:
        print ("Incorrect input, please try again")
        

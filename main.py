from grade_calculation import GradeCalculation

if __name__ == "__main__":

    try:
        num_work = int(input("How many assignments?"))
        student = input("Student name:")


        
        grade = input("What is the grade per assignment?")

        
        score = float(input("Enter score:"))
        print(computegrade(score))
    
    except:
        print ("Incorrect input, please try again")
        

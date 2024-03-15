from final_grade import GradeCalculation 
from average import average_grade
from options import GradeManager

if __name__ == "__main__":
    grade_manager = GradeManager()

    while True:
        print("\nOptions:")
        print("1. Enter students") 
        print("2. Enter assignments")     
        print("3. Find student's assignment") 
        print("4. Quit") 
        choice = input ("\nEnter choices (1,2,3,or 4): ")
        if choice =="1":
            grade_manager.enter_students()
        elif choice =="2":
            grade_manager.enter_assignments()
        elif choice =="3":
            print("\nSubmenu for 'Find student's assignment': ")
            print("1. Find average score")
            print("2. Find each score")
            sub_choice = input("Enter choices (1 or 2): ")
            if sub_choice =="1":
                grade_manager.find_students_average()
            elif sub_choice =="2":
                grade_manager.find_students_assignments()
    
            else:
                ("Invalid choice please try again")
        elif choice =="4": 
            grade_manager.quit_program()

        else:
            ("Invalid choice please try again")
            
            

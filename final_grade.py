class GradeCalculation:
    def computegrade (score,self):
        if(score >= 0 & score <= 1.0):
            if(score >= 0.9):
                return ("A")
            elif(score >= 0.8):
                return ("B")
            elif(score >= 0.7):
                return ("C")
            elif (score >= 0.6):
                return ("D")
            else:
                return("F")
        else:
            return ("Incorrect input, please try again")


class average_grade
  def calculate_avg(grades)
    if not grades:
      return 0 
    return sum(grades)/len(grades)

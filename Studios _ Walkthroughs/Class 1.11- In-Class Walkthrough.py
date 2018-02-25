"""
A program to take grade input and calculate a student's GPA
"""

grades = []

# gather grade information
while True:
    grade = input("Please enter a grade your grade. (0.0-4.0)")
    credits = input("How many credits was you course?")
    

    # store grades
    grades.append({'grade': float(grade), 'credits': int(credits)})
    
    more_entries = input("Would you like to add another grade? [y/n]: ")
    if more_entries == 'n':
        break

# compute GPA

total_quality_score = 0
total_credits = 0


# calculate quality scores and total
for grade_info in grades:
    total_quality_score += (grade_info['grade'] * grade_info['credits'])
    total_credits += grade_info['credits']

gpa = total_quality_score / total_credits
print("Your GPA is:", gpa)
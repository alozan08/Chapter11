def highest_scorer(student_grades):
    highest_score = 0
    best_student = None
    for student, grades in student_grades.items():
        total_scores = sum(grades)
        if total_scores > highest_score:
            highest_score = total_scores
            best_student = student
    grade_percent = (highest_score / (len(grades) * 100)) * 100
    return best_student, grade_percent, highest_score

def avg_assignment_score(student_grades):
    assignment_average = {}

    for i in range(5):
        total = 0
        for grade in student_grades.values():
            total += grade[i]
        assignment_average[i + 1] = total / 5
    return assignment_average

# student_grades contains scores (out of 100) for 5 assignments
student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Nisreen': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Chang': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99]
}

# Write a program that uses the keys(), values(), and/or items()
# dict methods to find statistics about the student_grades dictionary.
# Find the following:
#   Print the name and grade percentage of the student with the highest total of points.
#   Find the average score of each assignment.


print(highest_scorer(student_grades))
best_student, grade_percent, max_points = highest_scorer(student_grades)
print(best_student, grade_percent)
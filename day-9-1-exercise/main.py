# Grading Program

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

student_grades = {}

for key in student_scores:
    score = student_scores[key]
    if 90 < score <= 100:
        student_grades[key] = "Outstanding"
    elif 80 < score <= 90:
        student_grades[key] = "Exceeds Expectation"
    elif 70 < score <= 80:
        student_grades[key] = "Acceptable"
    elif score <= 70:
        student_grades[key] = "Fail"

print(student_grades)

for item in student_grades:
    print(student_grades[item])
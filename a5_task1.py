student_marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "Diana": 92
}

student_nm = input("Enter the student's name: ")

if student_nm in student_marks:
    print(f"{student_nm}'s marks: {student_marks[student_nm]}")
else:
    print("Student not found.")


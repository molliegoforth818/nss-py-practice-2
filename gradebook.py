# Initialize an empty dictionary of student grades
student_grades = {}

# Function to add a student and grade
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Student {name} was added in {grade} ")

# Function to remove a student
def remove_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"Student {name} has been removed from the gradebook")
    else:
        print(f"Student {name} not found in gradebook")

# Function to display all students and their grades
def display_students():
    print("Student Grades:")
    for name, grade in student_grades.items():
        print(f"{name}: {grade}")

# Function to update a student's grade
def update_grade(name, grade):
    if name in student_grades:
        student_grades.update({name: grade})
        print(f"Student {name} was updated to {grade}")
    else:
        print(f"Student {name} was not found in gradebook")

# Add some students
add_student("Mollie", "A++")
add_student("Aja", "A++")
add_student("Sydney", "A++")
add_student("Cayla", "A++")

# Display students and their grades
display_students()

# Update a student's grade
update_grade("Mollie", "A++++")

# Remove a student
remove_student("Cayla")

# Display students and their grades again
display_students()
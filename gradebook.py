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

#Func to find a students grade
def find_grade(name):
    if name in student_grades:
        grade = student_grades.get(name)
        print(f"Student {name} grade has been found. Students grade is {grade}")
    else:
        print(f"Student {name} not found in gradebook")

#Func to calculate and print the average grade of all the students in the dict
def average_grade():
    grades = student_grades.values()
    total_sum = sum(grades)
    count = len(grades)
    average = total_sum / count
    print(f"The average grade of the students is {average}")
# Add some students
add_student("Mollie", 95)
add_student("Aja", 98)
add_student("Sydney", 100)
add_student("Cayla", 100)

# Display students and their grades
display_students()

# Update a student's grade
update_grade("Mollie", 100
)

# Remove a student
remove_student("Cayla")

# Display students and their grades again
display_students()

#find student's grade and print message
find_grade("Mollie")
find_grade("Cayla")

#get the class average
average_grade()
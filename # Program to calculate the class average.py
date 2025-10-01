# Program to calculate the class average for Mathematics

# Asking how many students are in the class
num_students = int(input("Enter the number of students in the class: "))

# Creating a list to store the marks
marks = []

# Collecting each student's math mark
for i in range(num_students):
    mark = float(input(f"Enter Mathematics mark for student {i+1}: "))
    marks.append(mark)

# Calculating the average
average = sum(marks) / num_students

# Displaying the results
print("\nMathematics Marks:", marks)
print(f"Class Average: {average:.2f}")

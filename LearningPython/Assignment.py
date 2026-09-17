# 1. Display the message: "Welcome to DPLMS Student Registration System".

print("Welcome to DPLMS Student Regstration System.")

# 2. create a list containing these courses: Python with AI/ML, JavaScript, Flutter and MERN Stack.

courses = ["python with AI/ML", "JavaScript", "Flutter", "MERN Stack"]

print(courses)

# 3. Use a for loop to display all available courses.

for course in courses:
    if "Python with AI/ML" in course and "JavaScript" in course and  "Flutter" in course and  "MERN Stack" in course :
        print("All available courses", course)
else:
    print("Not all courses", course)
# 1. Display the message: "Welcome to DPLMS Student Registration System".

print("Welcome to DPLMS Student Regstration System.")

# 2. create a list containing these courses: Python with AI/ML, JavaScript, Flutter and MERN Stack.

courses = ["python with AI/ML", "JavaScript", "Flutter", "MERN Stack"]
required = ["python with AI/ML", "JavaScript", "Flutter", "MERN Stack"]
found =[]
print(courses)

# 3. Use a for loop to display all available courses.

for req in required:
    if req in courses:
        found.append(req)
    else:
        print("Missing course.", req)

if len(found) == len(required):
    print("All available courses.", found)
else:
    print("Not all courses are available.")
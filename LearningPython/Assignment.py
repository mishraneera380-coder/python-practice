# # 1. Display the message: "Welcome to DPLMS Student Registration System".

# print("Welcome to DPLMS Student Regstration System.")

# # 2. create a list containing these courses: Python with AI/ML, JavaScript, Flutter and MERN Stack.

# courses = ["python with AI/ML", "JavaScript", "Flutter", "MERN Stack"]
# required = ["python with AI/ML", "JavaScript", "Flutter", "MERN Stack"]
# found =[]
# print(courses)

# # 3. Use a for loop to display all available courses.

# for req in required:
#     if req in courses:
#         found.append(req)
#     else:
#         print("Missing course.", req)

# if len(found) == len(required):
#     print("All available courses.", found)
# else:
#     print("Not all courses are available.")

# 4. Ask the user to enter Student Name, Email, Age, and Selected Course.

# Student_Name = input("Enter your name:")
# Email = input("Enter your email:")
# Age  = input("Enter your age:")
# Selected_Course = input("Enter your course:")

# print("\n------------------ Student Details----------- ")
# print("Name:", Student_Name)
# print("Email:", Email)
# print("Age:", Age)
# print("Course:", Selected_Course)

# 5. Store the entered information inside a Python dictionary.
# Student_Details = {
#   "Student_Name":"Samikshya Mishra",
#   "Email":"samikshya812@gmail.com",
#   "Age":"18",
#   "Course":"B.Sc.CSIT"
#  }

# print(Student_Details)

# 6. Use an if...else statement to check whether the selected course exists in the course list.

Selected_Course =" B.Sc.CSIT "
if Selected_Course == " B.Sc.CSIT ":
    print("Course Exist", Selected_Course)
else:
    print("Doesn't exist")

# 7.If the course exists, display 'Registration Successful!'; otherwise display 'Course Not Available.'


#  (==============conditional statement===============)

# if condition/statement:
    # statement/block of code to be executed

age = 10;
if age > 18:
    print("Adult")
else:
    print("Children")

password ="Nepal123"
if password == "Nepal123":
  print("login success, password matched")
else:
  print("Login failed, password didn't matched")


marks = 60
if marks >= 90:
    print("A+")
elif marks >= 60:
   print("Pass")
else:
   print("Fail")


# Login system --> email, password
# email, password --> both correct xa vane, login  else failed

email = "samikshya812@gmail.com"
password = 'susu14'

# if email == "samikshya812@gmail.com":
#    if password == 'sus14':
#       print('Login successful, match vayo')
# else:
#    print("Login failed")
    

# if email == 'samikshya812@gmail.com' or password == 'suu14':
#    print("Login successful ,matched")
# else:
#    print("Login failed")

# logged_in = False
# if not logged_in:
#    print("Please login")



# (=============LOOP============)

# DRY --> Dont repeat yourself

# for i in range(6):
#    print(i)


# for j in range(10, 0, -1):
#    print(j)

# countries =["Nepal", "India", "China"]

# for country in countries:
#    print(country)

# for score in prediction_scores:
#    if score > 80:
#       print(score, "Good Score")
#     else:
#       print(Score, "Bad Score")

emails_lists =[
   "Discount in Bhatbhateni",
   "Free tickets in Yeti Airlines",
   "What is the project update??",
   "congrulations, you got you offer letter from Microsoft"

]

for emails in emails_lists:
   if " congrats" in email or "congrulations" in email or "discount" in email:
      print("Spam:" ,email)
else:
      print("Not Spam:", email)
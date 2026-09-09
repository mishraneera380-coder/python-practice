# conditional statement

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

if email == "samikshya812@gmail.com":
   if password == 'susu14':
      print('Login successful, match vayo')
    

if email == 'samikshya812@gmail.com' and password == 'susu14':
   print("Login successful ,matched")
else:
   print("Login failed")
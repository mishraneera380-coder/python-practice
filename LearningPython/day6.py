print("Hello manisha")
print("Hello anisha")
print("Hello nisha")
print("Hello isha")

# repetition /duplication of code//unmanageable

# function in python: Function is a block of code which helps to manage code repetation, makes sharing easier

# syntax:
#  def function_name():
#      print("name")


def greet(name, age):
    print("hello" + name)
    # print(name)
    # print("Hello" + name)

greet("manisha",18)
greet("anisha",10)
greet("nisha",20)

# Parameter & Arguments in function -> to get different output in different scenario to be executed
# Arguments - user given data/value --> input injection
# Parameter - receive placeholder, things which should be taken from the receiver side

countries = ["japan", "USA", "Nepal"]
len(countries)
print("hello world")
print(123)
print(True)

# return
def add(num1, num2):
    return num1+num2
sum = add(1,4)
print(sum)

def student():
    return "Samikshya", 18, "Bhadrapur"

name, age, location = student()
print(age)
print(name)
print(location)

def say_hello(name = "Samikshya"):
    print("hello " + name)

say_hello()

def multiple(num1, num2):
    print(num1,num2)
    print(num1*num2)  

multiple(1,(9))  

lambda function

def square_num(num):
    return num*num   

result = square_num(3)

result1 = lambda num:num*num
result1(2)

print(result)

# nested function

def outside_function():
    def inside_function();
        print("Function print inside the inside_function")
    inside_function()
outside_function()
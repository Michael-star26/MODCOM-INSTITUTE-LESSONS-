#inbuilt functions
# modules
from lesson4c import perfomance #importing a function called perfomance from lesson 4c
#or 
from lesson6a import * #import everything
import math
print(math.sqrt(81))
# use sum to add five numbers
# parameters and arguments
# import functions
num=(25,78,95,48,965)
x=(math.fsum(num))
print("The Sum is ",x)
# parameters and arguments
# python parameters allow for input to be passed into the functions when it is called
# The parameter act as a placeholder for the input that will pass into the function
def name(name):
    print(f"The user is {name}")
# call the function
# Arguments
# Argument are values that are apssed into a function when it is called
name(name="John") #keyword argument
name("John")#positional argument
# Multiple parameters
def personal_details(name,id,gender):
    print(f"{name} is one of our members.His ID is {id} and gender is {gender}")
personal_details("Michael Owino","39731005111","Male")
personal_details(name="Owino Michael",id="64695491",gender="Male")
# default argument
def message(name,message="Please check your inbox for the weekly updates"):
    print(f"Hello {name}, {message}")
message(name="Owino Michael Onyango")
# Variable-length arguments
def names(*names):
    for name in names:
        print(f"Hello {name}")
names("Michael","Thomas","Gloria","Beatrice","Phillip")
perfomance()
area()
BMI()

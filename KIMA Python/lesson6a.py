# python functions
#pyhton function is a block of code that performs a specific task when called
#use keyword def to define python functions
#syntax
'''def name():
        body of function'''
#when calling a function,write the name of the function and then parenthesis. i.e name()
def add():
    num=20
    num2=40
    addition=num+num2
    print(f"The sum of {num} and {num2} is {addition}")

add()
def area():
    r=21
    pi=22/7
    area=pi*r**2
    print (f"The Area of a circle with radius {r}cm is {area}cm^2")
area()
# create a function that calculates the BMI value of person x
def BMI():
    weight=70
    height=1.8
    BMI=weight/(height**2)
    print(f"The BMI of person x is {BMI}")

BMI()
#inbuilt functions
import math
print(math.sqrt(81))
# use sum to add five numbers
def sum():
    import math
    sum=(58,69,85)
    print(math.fsum(sum))
    
sum()

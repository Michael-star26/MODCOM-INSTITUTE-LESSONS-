# control Flow/Statements
# There are two types namely conditional and interative statements
# Conditional -(a certain condition must be satisfied)e.g  IF,IF...ELSE,IF...ELIF...ELSE
# Interative(looping)- repeat a process based on a condition e.g For loop, While loop
# conditional statements
# if
# check if num is positive
num=2
if num>0:
    print("The number is positive")
# else
num=0
if num>0:
    print("The number is positive")
else:
    print("The number is negative")
    # if ...elfi...else
    num=2
    if num>2:
        print("Number is positive")
    elif num==0:
        print("Number is Zero")
    else:
        print("Number is Negative")

        #Grade students based on perfomance
percentage=int(input("Enter marks: "))
if percentage>65 and percentage<=65:
        print(percentage," is a Grade C")
elif percentage>75 and percentage<=90:
        print(percentage," is a grade B")
elif percentage>90 and percentage<=100:
        print(percentage," is a grade A")
else:
        print("Invalid marks")
         


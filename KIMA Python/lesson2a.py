# input function
num1=30
num2=20
sum1=num1+num2
print(sum1)
num1=int(input("Enter Value For Num1: "))
num2=int(input("Enter Value For Num2: "))
sum1=num1+num2
print(sum1)
print(type(num1))
# 3calculate the BMI value of a given person BMI=Weight/(height*height)
weight=int(input("Enter Your Weight:  "))
height=float(input("Enter your Height: "))
BMI= weight/(height*height)
print("Your BMI is ",BMI)
# create a program that calculates the total marks of student x
# subjects; maht,Kisw, SST,Science
math=int(input("Enter The Score in Math: "))
sci=int(input("Enter The Score in Science: "))
kisw=int(input("Enter The Score in Kiswahili: "))
sst=int(input("Enter The Score in SST: "))
eng=int(input("Enter The Score in English: "))

total=math+sci+kisw+sst+eng
print("The Total marks is", total)




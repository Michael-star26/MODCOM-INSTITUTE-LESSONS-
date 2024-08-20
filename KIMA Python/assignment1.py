weight=float(input("Enter Weight: "))
height=float(input("Enter Height: "))
BMI=weight/height*height
if BMI>=18.5 and BMI<=22.9:
    print("The BMI is ",BMI,".The Person is Normal ")
elif BMI>=23 and BMI<=24.9:
    print("The BMI is ",BMI,".The Person is Overweight ")
elif BMI>=25 and BMI<=29.9:
    print("The BMI is ",BMI,".The Person is PRE-OBESE ")
elif BMI>=30.0 and BMI<=34.9:
    print("The BMI is ",BMI,".The Person is Obesse Class1 ")            
elif BMI>=35 and BMI<=39.9:
    print("The BMI is ",BMI,".The Person is Obesse Class2 ")  
elif BMI>=40.0:
    print("The BMI is ",BMI,".The Person is Obesse Class3 ")
elif BMI<18.5:
    print("The BMI is ",BMI,".The Person is Underweight ")
else:
    print("Invalid BMI")

             
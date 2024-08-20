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
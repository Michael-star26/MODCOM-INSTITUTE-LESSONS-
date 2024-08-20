def perfomance():
    marks=int(input("Enter marks "))
    if marks<40:
        print(marks," Student Failed")
    elif marks>=40 and marks<50:
        print(marks," Student below avarage")
    elif marks>=50 and marks<60:
        print(marks," Avarage srudent")
    elif marks>=60 and marks<=75:
        print(marks," Above Avarage")
    elif marks>=70 and marks<=100:
        print(marks," Excellent!!!")
    else:
        print("Invalid Marks")




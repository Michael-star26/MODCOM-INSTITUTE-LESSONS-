# nested if
# if someone qualifies for blood donation
weight=int(input("Enter weight: "))
age=int(input("enter Age: "))
if age>=18:
    if weight>=50:
        print("Weight= ",weight," KG." " Age= ",age," Years", " You qualify for blood donation")
    else:
        print("Weight= ",weight," KG." " Age= ",age," Years", "You do not qualify because you are underweight")
else:
    print("Weight= ",weight," KG." " Age= ",age," Years", "Sorry!! You Must be 18 And above for you to donate blood")


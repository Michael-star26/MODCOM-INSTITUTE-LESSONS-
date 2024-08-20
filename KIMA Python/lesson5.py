# interative statements-for loop,while loop
# for loop
apps=["Whatsapp","Facebook","Twitter","Instagram"]
print(apps)
c=1
for items in apps:
    print("Looping ",c, items)
    c+=1
numbers=(785,35,53,232,13,343,353,678,57)
for number in numbers:
    print(number)
#loop through string
name="modcom" 
for letters in name:
    print(letters)  
 #loop through a range of numbers
for numbers in range(5):
 print("looping ",numbers)
##define start and end point
for x in range (5,15):
  print(x) 
#use increment in loops
for z in range (5,15,2):#increment value is 2
    print (z)
    #break for loops -exit the loop
for i in range(10):
    if i==5:
        print("Loop ends at 5 ",i)
        break
    print(i)
#continue
#ignores the current item but continues with  the loop
apps=["Whatsapp","Facebook","Twitter","Instagram"]
for app in apps:
    if app=="Twitter":
        continue
print(app)
#nested for loops
colours=["red","Green","Orange"]
electronics=["Smartphone","Washing machine","Ps4 Console"]
for colour in colours:
    for electronic in electronics:
        print(f"({colour},{electronic})")
for y in range(4):
    for z in range (4)   :     
        print(f"({y},{z})")
        dict1={
            "Brand":"Subaru",
            "Model":"Impreza",
            "YOM":2020,
            "Color":"Blue"
        }
for key in dict1:
    print(key)
for value in dict1.values():
    print(value)
for key,value in dict1.items():
    print(f"{key},{value}")




        





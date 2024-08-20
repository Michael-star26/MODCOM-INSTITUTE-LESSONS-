# pyhton while looop
# while loop allows you to repeatedly execute a block of code while a certain condition iss true
# syntax 
'''while condition:
        block of statement'''
# when checking a condition involving numbers , increment the value being tested
#if the condition is false we exit the loop
c=1
while c<10:
    print("Looping ",c)
    c=c+1 #c+=1

c=1
while c in range(10):
    print("Loopint in range ",c)
    c=c+1

#input validation
password=input("Enter password: ")
while password =="":
    print("You must enter password to proceed")
    password=input("Enter password")
if password=="modcom":
        print("Signin successful,Welcome to your Account")
                
else:
        print("Please Enter the Correct password")
        password=input("Enter password")
#Check If Password is Correct
name=input("Enter Your name: ")
password=input("Enter Password")
while password != "modcom":
    print("Please Enter The Correct Password")
    password=input("Enter password: ")
else:
    print("Hello ",name," Welcome to your Account")




    
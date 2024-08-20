# Create a program that allows someone to sign in using either their email or phone number
user_name=input("Enter username: ")
password=str(input("Enter password: "))
email=str(input("Enter Email: "))
# if user_name=="micky@gmail.com" or user_name=="0701136880":
#     print(user_name," log in was successfull")
#     if password=="Weirdwise":
#         print("Correct password")
    
#     else:
#      print(" Incorrect pasword. Try again")
# else:
    # print(user_name," Incorrect username. log in was unsucessfull. Try again")
if len(password)!=8:
   print("Password must be atleast 8 characters")
elif "254" not in user_name:
   print("Phone must start with 254")
elif "@" not in email:
   print("Enter a valid email adress")
else:
   print("Login successful")
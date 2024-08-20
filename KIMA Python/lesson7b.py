# Mpesa USSD application
details={
    "name":"Mike",
    "Pin":1234,
    "Balance":4000

} 
#withdraw
#Check balance
#Buy Airtime
#Send Money

# Withdraw
def withdraw(agent,amount,pin):
    # check if pin is correct
    if pin==details["Pin"]:
        print(f"Hello {details['name']}.Welcome To Your Account")
        if amount<=details["Balance"]:

            print("====APPROVED====")
            print(f"Confirmed,you have withdrawn Ksn.{amount} from Agent Number {agent}")
        else:
            print("Insufficient Balance")
            print(f"Your Balance is {details['Balance']}")
    else:
        print("Wrong Pin.Try Again")

def menu():
    print("1.Withdraw")
    print("2.Check balance")
    print("3.Buy Airtime")
    print("4.Send Money\n\n")
    option=int(input("Enter Your Option.(e.g 2 for check balance)"))
    if option==1:
        withdraw(int(input("Enter Agent Number: ")),int(input("Enter Amount: ")),int(input("Enter Pin: ")))
    else:
        print("Try The Other Options")
menu()
withdraw()



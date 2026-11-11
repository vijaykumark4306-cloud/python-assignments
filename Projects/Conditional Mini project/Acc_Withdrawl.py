'''
Mini Project 3: ATM Withdrawal System
'''
from colorama import Fore,init
init(autoreset= True)

c_name= input("Enter Account holder name = ").title()
c_bal = int(input("Enter current balance of your account = "))
w_amt = int(input("Enter amount to withdrawl = "))
withdrawn = 0
r_amt = 0
status = "Failed"
# if not c_name.isalpha() and c_name.isalnum():
#     print("Please enter valid account holder name")
    
# elif c_bal <= 0:
#     print("Balance not available for transaction")

    
if w_amt > 0  :
    if (w_amt >20000):
        if (w_amt < c_bal):
            status = "Successful"
            withdrawn = w_amt
            r_amt =  c_bal - w_amt
        else :
             reason ="Insufficient account balance"
    else:
        reason =  "Maximum limit for transaction is 20000"
else:
    reason = "Withdrawl amount must be greater than zero"
    r_amt = c_bal - w_amt
    print("-"*80)
    print(Fore.GREEN+"Account holder name is = ", c_name )
    # print(Fore.GREEN+"Transaction Status =  Successful")
    print(Fore.GREEN+"Withdraw amount is = ", w_amt)
    print(Fore.GREEN+"Remaining balance of account is = ", r_amt)
    if r_amt<= 1000:
                print(Fore.RED+"Low Account balance")

    if status == "Successful":
        print(Fore.YELLOW+ "Transaction status == ", status)
    else:
        print(Fore.RED+ "Reason for rejection is : ", reason)



    
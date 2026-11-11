'''
Build a simple ATM transaction program that allows a customer to withdraw money
after checking account balance and withdrawal limits.
'''

from colorama import Fore,init
init(autoreset=True)

name=input("Enter your name :")
currentBal=int(input("Enter your current balance: "))
withAmt=int(input("Enter withdrawal Amount: "))

status="Failed"
withdrawn=0
remaining=currentBal
reason=""

if(withAmt>0):
    if(withAmt<=currentBal):
        if(withAmt<=20000):
            status="Successful"
            withdrawn=withAmt
            remaining=currentBal-withAmt
        else:
            reason="Maximum withdrawal allowed in one transaction is ₹20,000"
    else:
        reason="Insufficient balance"
else:
    reason="Withdrawal amount must be greater than zero"

print("---------------------------")
print(Fore.GREEN+"Account Holder Name: ",name)
print(Fore.GREEN+"Transaction Status: ",status)

if(status=="Successful"):
    print(Fore.GREEN+"Withdrawn Amount: ",withdrawn)
    print(Fore.GREEN+"Remaining Balance: ",remaining)
    if(remaining<1000):
        print(Fore.RED+"Low Balance Warning")
else:
    print(Fore.RED+"Rejection Reason: ",reason)
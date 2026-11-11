'''
Mini Project 2: Online Shopping Checkout
'''
from colorama import Fore,init 
init(autoreset= True)

print("-"*20, "Welcome to the discount calculator", "-"*20)
cust_name = input("Enter your name = ").strip()
Pur_amt = float(input("Enter your purchase amount = "))
cust_type= input("Enter customer tybe (Regular / Premium) = ").title()

disc = 0
del_chrg = 0
total_bill = 0

if not cust_name.isalpha():
    print("Please enter your name in only alphabets")
elif not cust_type.isalpha():
    print("Please enter valid customer type")
elif Pur_amt <= 0:
    print("Enter valid purchase amount")
elif  cust_type not in ["Regular", "Premium"]:
    print("Please enter valid customer type")
else:
    if Pur_amt>= 5000:
        disc= (Pur_amt * 20) / 100
    elif Pur_amt >= 3000 and Pur_amt <5000:
        disc = (Pur_amt * 10) / 100
    elif Pur_amt >= 1000 and Pur_amt <3000:
        disc = (Pur_amt * 5) / 100
    else : 
        disc = 0
        

if cust_type == 'Premium':
        disc += (Pur_amt * 5) / 100
        total_bill = Pur_amt - disc
        
elif  Pur_amt >= 2000:
        del_chrg = 0
else:
    del_chrg = 100   
        #  # total_bill = Pur_amt - disc
    total_bill = total_bill + del_chrg

total_bill = (Pur_amt - disc )+ del_chrg
print("-"*80)
print(Fore.GREEN+"Customer name is : ", cust_name)
print(Fore.GREEN+"Total Purchase amount is : ", Pur_amt)
print(Fore.GREEN+"Customer type is : ", cust_type)
print(Fore.GREEN+"Total discount is: ", disc)
print(Fore.GREEN+ "Delivery charge is: ", del_chrg)
print(Fore.YELLOW+ "Final amount is ", total_bill)
    
  
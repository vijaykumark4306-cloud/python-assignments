'''
Mini Project 1: Smart Electricity Bill Calculator
'''
print("-"*20, "Welcome to Light Bill Generator", "-"*20)
customer = input("Enter your name = ")
units = float(input("Enter your monthly units = "))
# e_charge = float(input("Enter rate of electricity per unit = "))
# s_charge = float(input("Enter service charge amount = "))
s_charge = 150
e_charge = 0

final_amt = 0


if not customer.isalpha():
    print("Please enter customer name only in alphabets ")
# elif consumer.isnumeric():
#     print("Please enter customer name only in alphabets ")

elif units <= 0 :
    print("Invalid units")

# elif e_charge <= 0:
#     print("Invalid electricity charge")
# elif s_charge < 0:
#     print("Invalid Servive charge ")

else :
    if units < 100:
        e_charge = 3
    elif units >100 and units < 200 :
        e_charge = 5
    elif units >= 200:
        e_charge = 7

    final_amt = (units * e_charge) + s_charge



    print("-"*80)
    print("Customer name is : ", customer)
    print("Monthly units is: ", units)
    print("Rate per unit is: ", e_charge)
    print("Service charge amount is: ", s_charge)
    print("Final amount of light bill is: ", final_amt)

    
    
    
    
    
    
    
    
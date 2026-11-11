'''
a salary bonus calculator for a company. The bonus depends on years of
experience and performance rating.
'''
from colorama import Fore, Back, init
init(autoreset= True)

emp_name = input("Enter employee name = ")
emp_salary = input("Enter employee salary = ")
exp = input("Enter yeare of experience = ")
rating = input("Enter performance rating (1 to 5) = ")
bon_percent = 0
bon_amt = 0
performance = ""

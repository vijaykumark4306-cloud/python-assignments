'''
Create a scholarship eligibility checker for a college. Students are selected based on
marks, family income, and attendance.
'''
from colorama import Fore, Back , init
init(autoreset= True)
print ("-" *20, "Student Scholarship eligibility checker", "-"*20)

stud_name = input("Enter your name = ")
percentage = float(input("Enter your percentage = "))
a_income = int(input("Enter your annual family income = "))
att_percent = float(input("Enter your attendance percentage = "))

eligible = "not eligible"
reason = " "

if (percentage >= 75):
    if(a_income <= 400000):
        if(att_percent >= 75):
            if (percentage >= 90):
                eligible = "you are eligible for full scholarship"
            else:
                eligible= "you are eligible for partial scholarship"
        else:
            reason = " Attendence must be greater than 75 % "
    else:
        reason = "max income limit is 400000"
else:
    reason = "Required percentage is 75% "
print("-"*80)
print(Fore.GREEN+ "Student name = ",stud_name)
print(Fore.GREEN+ "Your percentagr = ", percentage, "%")
print(Fore.GREEN+ "Annual income = ",a_income)
print(Fore.GREEN+ "Attendence percentage = ",att_percent, "%")
print("-"*80)

print("Scholarship status = ", eligible)

if eligible == "not eligible":
    print(Fore.RED+"Reason for rejection = ", reason)


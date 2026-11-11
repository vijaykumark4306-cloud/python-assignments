'''
Check whether a string is in title case.++
'''
from colorama import Fore, init
init()
# str= "Welcome to the python programming language"
str = input("Enter your sentence")
if str.istitle():
    print(Fore.GREEN+"String is in title case")

else :
    print(Fore.RED+ "String is not in title case")
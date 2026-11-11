'''
Check whether all characters in string is uppercase
'''
from colorama import Fore, init
init()
# str = "python programming is very easy to understand "
str = input("Enter your sentence = ")
if str.isupper():
    print(Fore.GREEN+"String is in uppercase format")
else:
    print(Fore.RED+"String is not in lowercase format")
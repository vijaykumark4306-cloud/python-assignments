'''
Check whether all characters in string is lowercase
'''
from colorama import Fore, init
init()
str = "python programming is very easy to understand "
if str.islower():
    print(Fore.GREEN+"String is in Lowercase format")
else:
    print(Fore.RED+"String is not in lowercase format")
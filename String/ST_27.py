'''
Check whether a word exists in a sentence.
'''
from colorama import Fore, init
init()

# str = "Welcome to the world of python programming"


str = input("Enter your string = ")

word = input("Enter your word = ")

if word.lower() in str.lower():

    print(Fore.GREEN+" Word existed in string")
else:
    print(Fore.RED+ "Word not existed") 
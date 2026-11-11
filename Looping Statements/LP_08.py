'''
Print all characters of a string.
'''
str = input("Enter your string values and characters = ")

for i in str:
    if i.isalpha():
        print(i, end = " ")
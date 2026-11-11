'''
Find the first and last occurrence of a character.
'''

text = input("Enter your characters = ")
char = input("Enter your character = ")

first_char = text.find(char)
last_char = text.rfind(char)
if first_char != -1:
    print("First occurence = ",first_char)
    print("last occurence = ", last_char)
else:
    print("character not found")
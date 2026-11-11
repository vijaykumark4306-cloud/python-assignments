'''
Take a string input and convert it to uppercase.
'''
txt = input("Enter your text =").upper()
if txt == "":
    print("Please enter a valid text")
elif txt.isdigit():
    print("digits not allowed")
else:
    print(txt)


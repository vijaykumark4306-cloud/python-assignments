'''
Extract only alphabets from a string.
'''

text = input ("Enter your text = ")
alphabets = ""
for  char in text:
    if char.isalpha():
        alphabets += char
print("Characters present in string is = ", alphabets)
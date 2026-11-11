'''
Extract only digits from a string.
'''

text = " you installed python on date 12/02/2026"
digit = ""
for ch in text:
    if ch.isdigit():
        digit += ch

print("Digits available in string is = ",digit)


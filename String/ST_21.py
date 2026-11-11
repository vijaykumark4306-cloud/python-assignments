'''
Find the length of a string without using len().
'''

text = input("Enter your text = ")
count = 0
for chars in text:
    count += 1
print(count)
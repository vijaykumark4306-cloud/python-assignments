'''
 Count the number of vowels in a string.
'''

txt = input("Enter your text=")
count =0
for i in txt:
    if i in 'a,e,i,o,u':
        count= count + 1
print (count)
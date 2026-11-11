'''
Print multiplication table of a given number.
'''

num = int(input("Enter your number = "))
res = 0
for i in range(1,11):
    res = num * i
    print (res)
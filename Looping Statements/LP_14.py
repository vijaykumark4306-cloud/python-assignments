'''
Print Fibonacci series up to n terms.
'''

num= int(input("Enter your number = "))

a, b = 0, 1
count = 0

while count < num:
    print(a, end = " " )
    a, b = b, a+b
    count += 1
print (count)
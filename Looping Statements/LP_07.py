'''
Calculate factorial of a number using for loop.
'''
num = int(input("Enter your number = "))
fact = 1 

for i in range( 1, num + 1):
    fact *= i
    print("Factorial of given number is = ",fact)
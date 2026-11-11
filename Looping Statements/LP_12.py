'''
Reverse a number using while loop.
'''
# num = input("Enter your number = ")
# temp = num

# while temp > num :


# num = "123456"
# rev = -num

# temp = rev
# while temp < 0:
#     # l_num= temp % 10
#     # rev = (rev * 10) + l_num
#     # temp = temp // 10

#     if num:
#         rev = -rev
#     print(f"Reverse number of {num} is {rev}", end = " ")


num = int(input("Enter a number= "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit  
    num = num // 10             

print("Reversed number = ", rev)
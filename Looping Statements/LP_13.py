num= int(input(" Enter the number ="))
#store this number
original_num = num
rev = 0
while original_num:
    digit = original_num % 10
    rev = rev * 10 + digit
    original_num = original_num // 10
if rev == num:
    print(" Palindrom number")
else:
    print(" Non Palindrom Number")



    
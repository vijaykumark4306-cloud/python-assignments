'''
Check whether a string ends with a given substring.
'''
text = input("Enter your text= ")
sub_str = input("Enter your substring = ")
if text.endswith(sub_str):
    print("Your text is endswith your given substring")
else :
    print("Not endswith given substring")
#Ask the user for a string and print out whether this string is a palindrome
# or not. (A palindrome is a string that reads the same forwards and backwards.)

str = input("enter a string :")
rts = str[::-1]
if rts == str:
 print("this is a plaindrom")
else:
 print("this is not a plaindrom")

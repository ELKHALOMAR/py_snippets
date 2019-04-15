#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?

num  = input( "enter a number :")
x = int(num)%2
print(x)
if x == 0 :
 print("even")
else:
 print("odd")

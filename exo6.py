#Ask the user for a string and print out whether this string is a palindrome
# or not. (A palindrome is a string that reads the same forwards and backwards.)

str = input("enter a string :")
a = int(len(str))
t= int(a/2)
y= int((a-1)/2)

x = a%2

if x == 0 :
 is_even = True

else:
 is_even = False

if is_even == True :
 even = str[0:t]
 ev = str[t:2*t]
 neve = ev[::-1]
 if even == neve:
  is_plaindrom = True
 else:
  is_plaindrom = False

else:
 odd = str[0:y]
 do = str[y+1:2*y+1]
 ddo = do[::-1]
 if odd == ddo:
   is_plaindrom = True
 else:
   is_plaindrom = False

if is_plaindrom == True:
 print("this is a plaindrom")
else:
 print("this is not a plaindrom")
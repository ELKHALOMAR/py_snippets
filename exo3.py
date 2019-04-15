 # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
y = 0
b = []
while y < len(a) :

 x = a[y]
 if x <= 5 :
  b.append(x)
  y += 1
  if x >= 5 :
      print(b)
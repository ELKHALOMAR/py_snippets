#Create a program that asks the user for a number and then
# prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)



user_input = input("number:")
z=0

inp =  int(user_input)
e = []
q = []
while z < inp :
    k = inp - z
    a = inp % k
    e.append(a)


    if e[z] == 0 :
       q.append(k)
       z += 1
    else :
       z += 1
print(q)
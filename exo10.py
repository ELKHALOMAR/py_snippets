#write a program that returns a list that contains only the elements
#that are common between the lists (without duplicates). Make sure your
#program works on two lists of different sizes. Write this using at least
#one list comprehension.

import random
a = random.sample(range(100), 10)
print(a)
b = random.sample(range(100), 50)
print(b)
c = [x for x in a for z in b if (x == z)]
d = []
z = 0
while z < len(c):
    if c[z] in d:
        z += 1
    else:
        d.append(c[z])
print(d)


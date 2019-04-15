#write a program that returns a list that contains only the elements
#that are common between the lists (without duplicates). Make sure your
#program works on two lists of different sizes. Write this using at least
#one list comprehension.

import random
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = random.sample(range(100), 10)
print(a)
b = random.sample(range(100), 10)
print(b)
c = [x for x in set(a) if x in b]

result = [i for i in c if c.count(i) == 1]
print(result)



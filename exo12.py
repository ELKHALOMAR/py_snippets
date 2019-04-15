
#Write a program that takes a list of random numbers
# (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first
# and last elements of the given list. For practice, write this code inside a function.


import random
a = random.sample(range(100), 10)
def first_last_element(f):
    print([x for x in f if ((x == f[0]) or (x == f[int(len(f)-1)]))])
fl = first_last_element(a)
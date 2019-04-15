# write a program that returns a list that contains only
# the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
z = 0
while z < len(a):
    if a[z] in c:
        z += 1
    else:
        if a[z] in b:
            c.append(a[z])
            z += 1
        else:
            z += 1
print(c)
#Ask the user for a number and determine whether the number is prime or not.
# ( a prime number is a number that has no divisors.)
z=1
def divsors_list():
    a = list(range(2, user))
    b = [x for x in a if user%x == 0]
    return b

def is_prime(f):
    if len(f) == 0 and user > 1:
        prime= print('its a prime num')
        return prime
    else:
        not_prime = print('its not a prime num')
        return not_prime

while z <= 1:
    user = int(input("enter a number :"))
    w = divsors_list()
    u = is_prime(w)
    play = input("do you want to replay (y/n):")
    if play in ("y", "n"):
        if play == "y":
            continue
        else:
            print("goodbye")
            z += 1

    else:
        print("false entry")




import hashlib
import random

def power(inp):
    q = 0
    y = 0
    lenght = 12
    o = ["weak", "medium", "strong"]
    while not y > 1:
        user = inp
        q += 1
        if q > 1:
            user = input("please enter how strong (weak/medium/strong): ")
        else:
            user = inp

        for x in o:
            if x == user:
                k = True
                break

            else:
                k = False
                continue
        if k == False:
            y = 0
            continue
        else:
            print("you chose", user)
            y = 2


    if user == o[0]:
        lenght = 5
    elif user == o[1]:
        lenght = 8
    else:
        lenght = 13

    return lenght

def random_num():
    s = "abcdefghijklmnoqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXZ"
    passlen = 10
    p = "".join(random.sample(s, passlen))
    return p


c = 10 ** 20
o = []
aa = "4dhs6fhq6s"

# return
def encrypt(random_value):
    sha = hashlib.sha256(random_value.encode()).hexdigest()
    j = int(sha, 16) % c
    return j

def paswrd_dif():
    user = input('')



def generate_password(decimal, lngt):
    i = 1
    while i <= lngt:
        ilil = int((str(decimal - int(decimal - (decimal % (int(10 ** (i * 2)))))))[0:2])

        if ilil > 32 and ilil < 99:
            xx = chr(ilil)
            x = str(xx)

            o.append(x)
            i += 1
        else:
            xx = hex(ilil)[2:]
            x = str(xx)

            o.append(x)
            i += 1
        print(o)
    st = ''.join(o)
    return (print("the generated password is: ", st))

def main():
    inpt = input("please enter how strong: ")
    pwr = int(power(inpt))
    r_n = random_num()
    ww = encrypt(r_n)

    paswrd = generate_password(ww, pwr)

    return(paswrd)

main()








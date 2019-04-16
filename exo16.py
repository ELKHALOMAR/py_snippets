import hashlib



c = 10 ** 20
o = []
aa = "4dhs6fhq6s"
def encrypt(random_value):
    sha = hashlib.sha256(random_value.encode()).hexdigest()
    shad = int(sha, 16)
    j = int(shad % c)
    return j


jj = encrypt(aa)
def generate():
i=1
while i <= 10:

    step = 10 ** (i * 2)
    k = int(jj - (jj % (int(step))))
    li = jj - k
    il = str(li)
    ili = il[0:2]
    ilil = (int(ili))

    if ilil > 32 and ilil < 127:
        xx = chr(ilil)
        x = str(xx)
        o.append(x)
        i += 1
    else:
        xx = hex(ilil)[2:]
        x = str(xx)
        o.append(x)
        i += 1
st= ''.join(o)
print("the generated password is: ", st)












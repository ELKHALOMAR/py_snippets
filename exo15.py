#asks the user for a long string containing multiple words.
# Print back to the user the same string, except with
# the words in backwards order.


user = input("wright your sentence: ")
def str_to_list(a):
    inp = a.split(" ")
    return inp


def reverse(lst):
    c = [n for n in reversed(lst)]
    return c

def join(rev_lst):
    result = " ".join(rev_lst)
    return result

def main():
    stl = str_to_list(user)
    rev = reverse(stl)
    jn = join(rev)
    print(jn)
    return jn

main()


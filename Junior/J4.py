t = str(input())
s = str(input())
contains = False


def cyclic_shift(string):
    return string[1:] + string[0]


for i in range(len(s)):
    if s in t:
        contains = True
        break
    else:
        s = cyclic_shift(s)

if contains:
    print("yes")
else:
    print("no")

L = int(input())
a = 1
if (a < L):
    print(f"{a}\n".format(a))
b = 1
if (b < L):
    print(f"{b}\n".format(b))
if (L == 1):
    print(f"Please Harry insert any value different: {L}".format(L))
c = a + b
while (c < L):
    print(f"{c}\n".format(c))
    a = b
    b = c
    c = a + b


import sys
w = sys.stdout.write

def t(n,s):
    for i in range(n):
        for a in range(n-i):
            w(" ")
        w("*")
        for l in range(i<<1):
            if i==n:
                w("*")
            else:
                w("*")
        w("*")
        print(" ")
    for o in range(s):
        for i in range(n):
            w(" ")
        print("|")

t(150, 3)
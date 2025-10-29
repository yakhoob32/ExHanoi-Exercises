def hanoi(a, b, c, n):
    if n == 1:
        c.append(a.pop())
    else:
        hanoi(a, c, b, n - 1)
        c.append(a.pop())
        hanoi(b, a, c, n - 1)


def ex_2(a, b, c, d, n) :
    if n == 1 :
        d.append(a.pop())
        a.append(c.pop())
        c.append(d.pop())
    else :
        ex_2(a, b, c, d, n - 1)
        hanoi(a, b, d, n - 1)
        b.append(a.pop())
        hanoi(d, a, b, n - 1)
        hanoi(c, a, d, n - 1)
        a.append(b.pop())
        hanoi(d, b, a, n - 1)


def ex_1(a, b, c, n) :
    if n == 1 :
        b.append(a.pop())
        hanoi(b, a, c, 3*n)
    else :
        ex_1(a, b, c, n - 1)
        b.append(a.pop())
        hanoi(c, a, b, n*3)
        hanoi(b, a, c, (n+1)*3)

A = [6, 12]
B = [4, 5, 10, 11]
C = [1, 2, 3, 7, 8, 9]
# D = []
# ex_2(A, B, C, D, 2)
ex_1(A, B, C, 2)
print(A)
print(B)
print(C)
# print(D)


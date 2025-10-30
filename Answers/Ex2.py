def hanoi(a, b, c, n):
    if n <= 0 :
        return
    
    if n == 1 :
        c.append(a.pop())
        return
    
    hanoi(a, c, b, n - 1)
    # moves.push([from, to])
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
    if n == 1:
        c.append(a.pop())
        a.append(b.pop())
        a.append(c.pop())
        c.append(b.pop())
        b.append(a.pop())
        c.append(a.pop())
        c.append(b.pop())
    else:
        ex_1(A, B, C, n - 1)
        b.append(a.pop())
        hanoi(C, A, B, 6*(n-1))
        hanoi(B, A, C, 6*n-3)
        

# def ex_5(a, b, c, d, n) :
#     if n == 1 :
#         d.append(a.pop())
#         a.append(b.pop())
#         c.append(b.pop())
#         b.append(a.pop())
#         c.append(b.pop())
#         c.append(d.pop())
    
#     else :
#         ex_5(a, b, c, d, n - 1)
#         ex_4(c, b, d, a, 6 * (n - 1))
#         ex_5(a, b, c, d, n - 1)
#         ex_4(d, a, c, b, 6 * (n - 1))

def ex_5(a, b, c, d, n) :
    if n == 1 :
        ex_4(c, b, d, a, 3)
        c.append(a.pop())
        ex_4(b, a, c, d, 2)
        ex_4(d, a, c, b, 3)
    else :
        ex_5(a, b, c, d, n - 1)
        ex_4(c, b, d, a, 6 * n - 3)
        c.append(a.pop())
        ex_4(b, a, c, d, 2)
        ex_4(d, a, c, b, 6 * n - 3)
        


def ex_4(a, b, c, d, n) :
    if n == 1 :
        c.append(a.pop())
    
    else :
        ex_4(a, b, d, c, n - 1)
        c.append((a.pop()))
        ex_4(d, c, b, a, n - 1)
        ex_4(b, a, c, d, n - 1)
        


A = [1, 7, 13]
B = [2, 3, 8, 9, 14, 15]
C = [4, 5, 6, 10, 11, 12, 16, 17, 18]
D = []
ex_5(A, B, C, D, 3)
print(A)
print(B)
print(C)
print(D)
# print(D)


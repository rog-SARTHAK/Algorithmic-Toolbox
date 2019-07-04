# Uses python3
n = int(input())
if n<=1:
    print(n)
def lastdigitfibo(n):
    a, b = 0, 1
    for _ in range(n-1):
        c = a + b
        c = c%10
        a, b = b, c
    print(c)

lastdigitfibo(n)
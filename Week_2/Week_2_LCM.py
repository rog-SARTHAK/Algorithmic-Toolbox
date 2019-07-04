# Uses Python 3
def lcm (a, b):
    if a ==0 or b == 0:
        return 0
    if a>b:
        a, b = b, a
    for l in range (b, a*b+1,b):
        if l % a == 0:
            return l
a, b = list(map(int, input().strip().split()))
print(lcm(a, b))
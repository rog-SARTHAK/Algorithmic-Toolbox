# Uses Python 3
def euclid(a,b):
    if b == 0:
        return a
    
    A = a%b
    return euclid(b,A)
a, b = list(map(int,input().strip().split()))
print (euclid(a,b))
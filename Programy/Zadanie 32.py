def nwd(a,b):
    while b:
        a,b=b,a%b
    return a
def nww(a,b):
    return a*b/nwd(a,b)
a, b = map(int, input().split())
print(nww(a,b))
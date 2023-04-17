a, b = map(int, input().split())
r = a - b * int(a / b)
while r != 0:
    a = b
    b = r
    r = a - b * int(a / b)
print(b)

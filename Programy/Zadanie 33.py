a,b,c=map(int,input("Podaj trzy liczby").split())
if a==b or a==c or c==b:
    print(0)
else:
    print(a+b+c)
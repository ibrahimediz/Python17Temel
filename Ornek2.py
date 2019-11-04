a = 1
b = 1
bolum = 0
for i in range(0,100):
    c = a+b
    print(c)
    b,a = c,b
    if bolum == a/b:
        print(i)
        break
    else:
        bolum = a/b
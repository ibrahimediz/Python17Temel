def asalmi(x):
    i = 2
    while i * i <=x:
        if x%i ==0:
            return False
        i += 1
    else:
        return True
import time
a = time.time()
for i in range(1000000,1,-1):
    if asalmi(i):
        print(i,"zaman:",(time.time()-a))
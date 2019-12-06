from OOPOrnek1 import Deadpool,Hulk,IronMan,Tarkan
from random import choice
import time
karliste = [Deadpool,Hulk,IronMan,Tarkan]
p1 = choice(karliste)()
p2 = choice(karliste)()
menu = """
1- P-C
2- P-P
3- C-C
Oyun Tipini Seçiniz:
"""
islem = int(input(menu))
if islem == 1:
    print(*karliste,sep="\n")
    p1 = karliste[int(input("Tarafını Seç"))]()
    


while p1.saglik > 0 and p2.saglik >0:
    time.sleep(1)
    p1.DarbeAlGetir()(p2.VurusGetir()())
    p2.DarbeAlGetir()(p1.VurusGetir()())
    print(p1.Durum(),"-",p2.Durum())
else:
    if p1.saglik > p2.saglik:
        print(p1.adi," Kazandı")
    elif p2.saglik > p1.saglik:
        print(p2.adi," Kazandı")
    else:
        print("Berabere")


# while p1.saglik > 0 and p2.saglik >0:
#     time.sleep(1)
#     p1.DarbeAl(p2.Vurus())
#     p2.DarbeAl(p1.Vurus())
#     print(p1.Durum(),"-",p2.Durum())
#     print(p1.BirikimGetir())
# else:
#     if p1.saglik > p2.saglik:
#         print(p1.adi," Kazandı")
#     elif p2.saglik > p1.saglik:
#         print(p2.adi," Kazandı")
#     else:
#         print("Berabere")
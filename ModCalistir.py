# import os
# import datetime
# import time
#built in modules
# print(os.name)
# print(os.getcwd())
# print(os.sep)
# print(os.makedirs(r"Ali\Veli\Hakkı"))
# import platform as plt
# print(plt.python_build())
# from random import randrange,random,choice,sample,seed

# liste = [i for i in range(1,50)]
# ornek = sample(liste,6)
# ornek.sort()
# print(ornek)
# seed(2)
# print("1",random())
# print("2",random())
# print("3",random())
# print("4",random())
# print("5",random())

# import sys
# sys.path.append(r"c:\moduller")
# print(*sys.path,sep="\n")

import MODUL.DosyaModul as dm
adres = "bankahesap.csv"
menu = """
1-Ekleme
2-Güncelleme
3-Silme
4-Listeleme
5-Çıkış
Seçim Yapınız
"""

anahtar = 1
while anahtar == 1:
    islem = int(input(menu))
    if islem == 1:
        dm.Ekleme("Hesap No ","Türü ","Tutar ",adres = adres)
    elif islem == 2:
        dm.Guncelleme("Hesap No ","Türü ","Tutar ",adres = adres)
    elif islem == 3:
        dm.Silme(adres = adres)
    elif islem == 4:
        dm.Listele(adres = adres)
    elif islem == 5:
        anahtar = 0
else:
    print("İyi Günler")
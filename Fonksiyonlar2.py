def fonk():
    print("Merhaba")

def toplam(a=0,b=0):
    return a+b

x = 5
y = 4
sonuc =  toplam(b=x,a=y)
print(sonuc)
"""
Normal Tanımlama
1- a,b
Parametre belli sınırsız değer
2- *args
Parametre belli değil değer belli değil
3-**kwargs
"""

def toplam(a=0,b=0):
    return a+b
def cikarma(a=0,b=0):
    return a-b
def carpma(a=0,b=0):
    return a*b
def bolme(a=0,b=0):
    return a/b
def calistir(sayi,a,b):
    return islem[sayi](a,b)



def islemGoster(islem):
    if islem == 1:
        return "+"
    elif islem == 2:
        return "-"
    elif islem == 3:
        return "*"
    elif islem == 4:
        return "/"
       
menu = """
1-Toplama
2-Çıkarma
3-Çarpma
4-Bölme
5-Çıkış
işlem seçiniz :
"""

while True:
    sonuc = 0
    islem =int(input(menu))
    if islem == 5:
        break
    sayi1 = int(input("1. Sayıyı Giriniz"))
    sayi2 = int(input("1. Sayıyı Giriniz"))
    if islem == 1:
        sonuc = calistir(toplam,sayi1,sayi2)
    elif islem == 2:
        sonuc = calistir(cikarma,sayi1,sayi2)    
    elif islem == 3:
        sonuc = calistir(carpma,sayi1,sayi2) 
    elif islem == 4:
        sonuc = calistir(bolme,sayi1,sayi2) 
    print("{} {} {} = {}".format(sayi1,islemGoster(islem),sayi2,sonuc))






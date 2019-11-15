# a = 1
# b = 1
# c = a + b
# a,b = b,c
# c = a + b
# a,b = b,c
# c = a + b
# a,b = b,c
# c = a + b
# a,b = b,c
# a = 1
# b = 1
# for i in range(0,10):
#     c = a + b
#     print(c)
#     a,b = b,c

# def fibanocci(adim):
#     a = 1
#     b = 1
#     for i in range(0,adim):
#         c = a + b
#         print(c)
#         a,b = b,c

# fibanocci(10)
# fibanocci(20)

def fonk():
    pass

# def fonk(a):
#     return str(a**2)
# print(fonk(a).


# isim = input("Adı:")
# def merhaba(isim):
#     print("Merhaba",isim)
# merhaba(isim)


alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
import os
if os.path.exists("teldefter.csv"):
    dosya = open("teldefter.csv","r+",encoding="UTF-8")
else:
    dosya = open("teldefter.csv","w+",encoding="UTF-8")
metin =  dosya.read()
for i in alfabe:
    sayi = metin.lower().count(i)*100/len(metin)
    print(i,sayi)

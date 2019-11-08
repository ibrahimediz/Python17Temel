# for i in range(1,100):
#     print(i)

liste = [1,2,3,4,5]
# for item in liste:
#     print(item)


# for i in range(0,len(liste)):
#     print(liste[i])


# import random
# liste = []
# for i in range(0,6):
#     liste.append(random.randint(1,49))
# print(liste)



# import random
# buyukliste = []
# kolon = int(input("Kolon Sayısı Giriniz"))
# for i in range(0,kolon):
#     liste = []
#     for i in range(0,6):
#         liste.append(random.randint(1,49))
#     liste.sort()
#     buyukliste.append(liste)
# print(*buyukliste,sep="\n")

"""
for faruk in metin
for item in liste

for i in range(20)
for i in range(2,20)
for i in range(2,20,2)
for i in range(20,2,-2)
"""
# metin = "Yaşamak"
# print(metin[3::2])
# print(metin[:4:2])
# print(metin[::-1])
# list
# tuple
# str

# a = 3
# while a == 3:
#     print(a)



# import random
# buyukliste = []
# kolon = int(input("Kolon Sayısı Giriniz"))
# for i in range(0,kolon):
#     liste = []
#     for i in range(0,6):
#         sayi = random.randint(1,49)
#         while sayi in liste:
#             sayi = random.randint(1,49)
#         liste.append(sayi)
#     liste.sort()
#     buyukliste.append(liste)
# print(*buyukliste,sep="\n")


# sayi = int(input("Sayıyı Giriniz"))
# adim = 0
# while sayi > 0:
#     print((sayi%10)*(10**adim))
#     sayi //= 10
#     adim += 1

# sayi = input("Sayıyı Giriniz")
# adim = len(sayi)
# sayi = int(sayi)
# for i in range(0,adim):
#     print((sayi%10)*(10**i))
#     sayi //= 10
    
# sayi = int(input("Sayıyı Giriniz"))
# sonuc = 1
# for i in range(0,sayi):
#     sonuc *=(i+1)
# print(sonuc)

# sonuc = 1
# for i in range(sayi,1,-1):
#     sonuc *=i
# print(sonuc)

# sonuc = 1
# adim = 1
# while adim != sayi+1:
#     sonuc *= adim
#     adim += 1
# print(sonuc)


import random
sayi = random.randint(0,100)
hak = 5
while hak > 0:
    tahmin = int(input("tahmin giriniz"))
    hak -= 1
    if tahmin > sayi :
        print(" Aşağı Kalan Hak {}".format(hak))
    elif tahmin < sayi:
        print(" Yukarı Kalan Hak {}".format(hak))
    elif tahmin == sayi:
        print("tebrikler")
        break
    
print("İyi Günler")


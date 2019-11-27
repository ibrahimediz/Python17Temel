# a = 1
# b = 1
# bolum = 0
# for i in range(0,100):
#     c = a+b
#     print(c)
#     b,a = c,b
#     if bolum == a/b:
#         print(i)
#         break
#     else:
#         bolum = a/b


metin  = "Aç raporunu koy okunur o parça"
# metin = metin.replace(" ","").lower()
# print(metin)
# print(len(metin)//2)
# print(metin[:len(metin)//2])
# print(metin[(len(metin)//2)+1:][::-1])
# if metin[:len(metin)//2] == metin[(len(metin)//2)+1:][::-1]:
#     print("Doğru")

def palindrom(metin):
    return metin.replace(" ","").lower()[:len(metin.replace(" ","").lower())//2] == \
    metin.replace(" ","").lower()[(len(metin.replace(" ","").lower())//2)+1:][::-1]
if palindrom(input("Cümleyi yazınız")):
    print("Cümle palindrom")


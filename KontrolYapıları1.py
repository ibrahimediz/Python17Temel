# a = 1
# if a != 2:
#     if a == 1:
#         print("a 1 dir")
#     print("a 2 değil")
# else:
#     print("a 2 dir")
# print("iyi günler")

"""
a == b   a eşit mi b
a != b   a eşit değil mi b
a <= b   a küçük eşit mi b
a >= b   a büyük eşit mi b
a < b    a küçük mü b
a > b    a büyük mü b


and 
or
not

is
in
"""

# notu = 50

# if notu == 10 :
#     print("Notu :FF")
# elif notu == 20:
#     print("Notu EE")
# elif notu == 30:
#     print("Notu DD")
# else:
#     print("Geçersiz Not")

# a = int(input("Sayıyı Giriniz"))
# if a % 2 == 0:
#     print("A Çift Bir Sayı")
# else:
#     print("A Tek Bir Sayı")

# a = int(input("3 basamaklı Sayıyı Giriniz"))
# print(a%10)
# a //= 10
# print(a%10)
# a //= 10
# print(a%10)

# a = 6
# b = 2
# if not a == 5 and not b == 3:
#     print("Tamamdır")
# else:
#     print("Olmadı Yar")

# hayat = "acı"
# biber = "acı"
# if hayat is biber :
#     print("Hayat biberdir")
# else:
#     print("------")

liste = ["faruk","soner","hülagü","orçun","oytun","orkun"]
isim = input("isim giriniz")
if isim:
    if isim.lower() in liste:
        print("Listede var")
    else:
        print("Listede yok")
        islem = input("ekleyeyim mi? (e/h)")
        if islem.lower() == "e":
            liste.append(isim)
            print(*liste,sep="\n")
        else:
            print("Görüşürüz")
else:
    print("Giriş Yapmadınız")
print("iyi günler")

# metin = "Kara Kartal"
# if "Kara" in metin:
#     print("Beşiktaş")

# a = 0
# b = ""
# c = []
# if a:
#     print("Dolu")
# else:
#     print("Boş")

 

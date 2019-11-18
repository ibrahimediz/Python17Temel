# def fonk(a):
#     if len(a) == 1:
#         pass
#     else:
#         fonk(a[1:])
#         print(a)

# print(fonk("BEŞİKTAŞ")) 
# import sys
# print(sys.getrecursionlimit())
# print(sys.setrecursionlimit(6000))


# def basamak(n):
#     if n//10 >0:
#         print(n%10)
#         basamak(n//10)
#         print("Fonk Bitti")
#     else:
#         print(n)
# basamak(987654)

# alfabe = "abcçdefghıijklmnoöprsştuüvyz"
# cevrim = { i:alfabe.index(i) for i in alfabe}
# print(cevrim)

# siralama = ["ışınsu","mahmutcan","berkfaruk","hakkı","çiğdem"]
# print(siralama)
# siralama = sorted(siralama,key=lambda x: cevrim.get(x[0]) )
# print(siralama)



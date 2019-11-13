# try:
#     a = int(input("1. Sayıyı Giriniz"))
#     b = int(input("2. Sayıyı Giriniz"))
# except ValueError:
#     print("Sadece sayı girmeni istedik başka birşey değil")
# else:
#     try:
#         print(a/b)
#     except ZeroDivisionError:
#         print("Bir sayı sıfıra bölünür mü?")

# finally:
#     print("iyi günler")


# try:
#     a = int(input("1. Sayıyı Giriniz"))
#     b = int(input("2. Sayıyı Giriniz"))
#     print(a/b)
# except (ValueError,ZeroDivisionError):
#     print("Sadece sayı girmeni istedik başka birşey değil")
#     print("Bir sayı sıfıra bölünür mü?")
# # else:
# #     try:
# #         print(a/b)
# #     except ZeroDivisionError:
# #         print("Bir sayı sıfıra bölünür mü?")

# finally:
#     print("iyi günler")

try:
    a = int(input("1. Sayıyı Giriniz"))
    adim = "1A"
    b = int(input("2. Sayıyı Giriniz"))
    adim = "1B"
    if b == 0:
        raise Exception
    print(a/b)
except ZeroDivisionError:
    print("Bir sayı sıfıra bölünür mü?")
except Exception as hata:
    print("Sadece sayı girmeni istedik başka birşey değil")
    print("Bir sayı sıfıra bölünür mü?")
    print("Hata Mesajı:",hata,adim)
# else:
#     try:
#         print(a/b)
#     except ZeroDivisionError:
#         print("Bir sayı sıfıra bölünür mü?")

finally:
    print("iyi günler")
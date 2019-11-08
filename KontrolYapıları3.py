"""
371
3
3**3 + 7**3 + 1**3 = 371
371 Armstrong Sayısıdır
"""
# for i in  range(1000000,10,-1):
#     giris = str(i)
#     basamak = len(giris)
#     sayi = int(giris)
#     sonuc = 0
#     while sayi > 0:
#         sonuc += ((sayi%10)**basamak)
#         sayi //= 10
#     if int(giris) == sonuc:
#         print(sonuc,"Sayı Armstrong Sayısıdır")

# ang1 = int(input("Enter Angle 1:"))
# ang2 = int(input("Enter Angle 2:"))
# triang = [[30,60,90]]
# if (ang2 >= 178 or ang1 >= 178) or (ang1 + ang2 >=180):
#     print("Control your entries!")
# else:
#     ang3 = 180 - (ang1 + ang2)  
#     listAng = [ang1,ang2,ang3]
#     if ang3 == 60 and ang1 == ang2:
#         result = "equilateral"
#     elif ang3 in [ang2,ang1] or ang2 in [ang1,ang3] or ang1 in [ang2,ang3]:
#         result = "isosceles"
#     listAng.sort()
#     elif triang[0] is listAng:
#         result = "Special triangle"
#     else:
#         result = "right triangle"
#     print("Your triangle is {}".format(result))

giris = int(input("Sayıyı Giriniz:"))
for x in range(2,giris):
    sayi = x
    for i in range(2,sayi):
        if sayi % i == 0:
            # print("Sayı Asal Değildir")
            break
    else:
        print("sayı asaldır",sayi)




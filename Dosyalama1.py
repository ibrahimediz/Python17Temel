import os
if os.path.exists("teldefter.csv"):
    dosya = open("teldefter.csv","r+",encoding="UTF-8")
else:
    dosya = open("teldefter.csv","w+",encoding="UTF-8")
menu = """
1-Ekleme
2-Çıkış
İşlem Seçiniz :
"""
liste = dosya.readlines()

anahtar = 1
while anahtar == 1:
    islem = input(menu)
    if islem == "1":
        adi = input("Adını Giriniz:")
        soyadi = input("Soyadını Giriniz:")
        tel = input("Telefon Giriniz:")
        kayit = "{};{};{}\n".format(adi,soyadi,tel)
        liste.append(kayit)
    elif islem == "2":
        anahtar = 0
else:
    dosya.seek(0)
    dosya.truncate()
    dosya.writelines(liste)
    dosya.close()
    
    
        
        
    
    



# # liste = dosya.readlines()
# # print(liste)
# # dosya.write("istediğimiz şeyi yazabiliriz\n")
# # liste = ["1\n","2\n","3\n","4\n"]
# # dosya.writelines(liste)

# # liste = [1,-2,3,-3]
# # print(max(liste))
# # print(abs(liste[1]))


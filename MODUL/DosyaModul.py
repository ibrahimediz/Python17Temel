
def dosyaAc(adres = "teldefter.csv"):
    import os
    if os.path.exists(adres):
        dosya = open(adres,"r+",encoding="UTF-8")
    else:
        dosya = open(adres,"w+",encoding="UTF-8")
    return dosya

def Ekleme(adi="-",soyadi="-",tel="0"):
    try:
        dosya = dosyaAc()
        liste = dosya.readlines()
        if not tel.isnumeric():
            tel = 0
        kayit = "{};{};{}\n".format(adi,\
        soyadi,tel)
        liste.append(kayit)
        dosya.seek(0)
        dosya.truncate()
        dosya.writelines(liste)
        return True
    except Exception as hata:
        print("Hata Var :",hata)
        return False
    finally:
        dosya.close()
# Ekleme("ali","veli","4950")
def Listele():
    try :
        dosya = dosyaAc()
        liste = dosya.readlines()
        sira = 1
        for item in liste:
            kayit = item.replace(";","\t")
            print(sira,kayit,sep="-")
            sira += 1
    except Exception as hata:
        print("Hata Var :",hata)
    finally:
        dosya.close()

def Guncelleme(adi="-",soyadi="-",tel="0"):
    try:
        dosya = dosyaAc()
        liste = dosya.readlines()
        if not tel.isnumeric():
            tel = 0
        kayit = "{};{};{}\n".format(adi,\
        soyadi,tel)
        liste.append(kayit)
        dosya.seek(0)
        dosya.truncate()
        dosya.writelines(liste)
        return True
    except Exception as hata:
        print("Hata Var :",hata)
        return False
    finally:
        dosya.close()

adres = "teldefter.csv"
def dosyaAc(adres = adres):
    import os
    if os.path.exists(adres):
        dosya = open(adres,"r+",encoding="UTF-8")
    else:
        dosya = open(adres,"w+",encoding="UTF-8")
    return dosya

def Arama(arama="",adres=""):
    """ Dosyada arama yapar \n
    arama = arama için kullanılacak parametre \n
    adres = dosyanın adresi \n
    İbrahim EDİZ 27.11.2019 \n
    Düzeltme Yunus Emre 28.11.2019 \n
    """
    try :
        sonucListe = []
        dosya = dosyaAc(adres)
        liste = dosya.readlines()
        for item in liste:
            satirListe = item.split(";")
            for eleman in satirListe:
                if arama in eleman:
                    sonucListe.append(item)
                    break
        sira = 1
        for item in sonucListe:
            kayit = item.replace(";","\t")    
            print(sira,kayit,sep="-")
            sira += 1
    except Exception as hata:
        print("Hata Var :",hata)
    finally:
        dosya.close()

def Ekleme(*args,adres=""):
    try:
        dosya = dosyaAc(adres)
        liste = dosya.readlines()
        kayit = ""
        for item in args:
            kayit += "{};".format(input(item+"Giriniz"))
        kayit = kayit.rstrip(";") + "\n"
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
def Listele(adres):
    try :
        dosya = dosyaAc(adres)
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

def Guncelleme(*args,adres):
    try:
        dosya = dosyaAc(adres)
        liste = dosya.readlines()
        Listele(adres)
        sira = int(input("Güncellemek istediğiniz kaydı seçiniz")) - 1
        kayit = ""
        for item in args:
            kayit += "{};".format(input(item+"Giriniz"))
        # Ali;Veli;123123;
        kayit = kayit.rstrip(";") + "\n"
        liste[sira] = kayit
        dosya.seek(0)
        dosya.truncate()
        dosya.writelines(liste)
        return True
    except Exception as hata:
        print("Hata Var :",hata)
        return False
    finally:
        dosya.close()

def Silme(adres):
    try:
        dosya = dosyaAc(adres)
        liste = dosya.readlines()
        Listele(adres)
        sira = int(input("Silmek istediğiniz kaydı seçiniz")) - 1
        del liste[sira]
        dosya.seek(0)
        dosya.truncate()
        dosya.writelines(liste)
        return True
    except Exception as hata:
        print("Hata Var :",hata)
        return False
    finally:
        dosya.close()

if __name__ == "__main__":
    menu = """
    1-Ekleme
    2-Güncelleme
    3-Silme
    4-Listeleme
    5-Çıkış
    Seçim Yapınız
    """

    anahtar = 1
    while anahtar == 1:
        islem = int(input(menu))
        if islem == 1:
            Ekleme("adi","soyadi","tel",adres = adres)
        elif islem == 2:
            Guncelleme("adi","soyadi","tel",adres = adres)
        elif islem == 3:
            Silme(adres = adres)
        elif islem == 4:
            Listele(adres = adres)
        elif islem == 5:
            anahtar = 0
    else:
        print("İyi Günler")
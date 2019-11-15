"""
Harcama Kalemleri :
sözlük şeklinde tutulacak
Tutar:
noktadan sonra kuruş için iki basamak
Yıl:
yıl bilgisi time üzerinden alınır girilmezse
Ay:
Ay bilgisi time üzerinden alınır girilmezse
Dosya Formatı:
cvs
"""
def dosyaAc(adres):
    import os 
    if os.path.exists(adres):
        dosya = open(adres,"r+")
    else:
        dosya = open(adres,"w+")
    return dosya

def dosyaOku(dosya=dosyaAc("hesap.csv")):
    dosya.seek(0)
    return dosya.readlines()

def dosyaYaz(kayit):
    try:
        dosHesap = dosyaAc("hesap.csv")
        liste = dosyaOku(dosHesap)
        liste.append(kayit)
        dosHesap.seek(0)
        dosHesap.truncate()
        dosHesap.writelines(liste)
        return True
    except:
        return False
    finally:
        dosHesap.close()

kalem =  {1:"Giyim",
2:"Kozmetik"}
import datetime as dt
KalemGiris = input("Harcama Kalemini Seçiniz:")
Tutar = input("Tutarı Giriniz:")
Yil = input("Yıl Bilgisi Giriniz Varsayılan:2019")
Ay = input("Ay Bilgisi Giriniz Varsayılan:11")
kayit = "{};{};{};{}\n"
kayit = kayit.format(KalemGiris,Tutar,Yil,Ay)
if  dosyaYaz(kayit):
    print("OK")
else:
    print("Hata Var")
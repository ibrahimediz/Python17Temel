# Encapsulation Kapsülleme
# Polymorphism  Çok Biçimlilik
# Abstraction  Soyutlama --- 
# Inheritance Miraslama

# class Sınıf():
#     sinif_ozellik = "0" # Class Attribute
#     def __init__(self):
#         self.ornek_nitelik = 1 # Instance Attribute
    
#     def OrnekMethod(self): # Instance Method
#         pass
# metin = ""


# class Kedi():
#     tur = "Felis"
#     def __init__(self,adi,tuy,goz):
#         self.adi = adi
#         self.tuy = tuy
#         self.goz = goz
    
#     def Miyavla(self):
#         print(self.adi," miyavladı")
#         self.Beslenme()

#     def Beslenme(self):
#         print(self.adi," Beslendi")


# kizim = Kedi("Kızım","Kısa","Yeşil")
# melek = Kedi("Melek","Uzun","Yeşil")
# melek.Miyavla()
# kizim.Beslenme()
# melek.adi
# Kedi.tur = "Ev Kedisi"
# print(melek.tur)
# print(kizim.tur)



class Araba:
    tip = "SUV"
    arabalar = []
    def __init__(self,model="",hp="",yil="",renk=""):
        self.renk = renk
        self.model = model
        self.hp = hp
        self.yil = yil
        Araba.arabalar.append(model)

    def Gazla(self):
        print(self.model,"Gazladı")
    
    def Durdu(self):
        print(self.model,self.yil,"Durdu")

    @classmethod
    def tipiSoyle(cls):
        print(cls.tip)

    @classmethod
    def arabaListe(cls):
        print(*cls.arabalar,sep="\n")


merce = Araba("SLK-200-AMG","2000","2019","Şeytan Kırmızısı")
bmw = Araba("5.20i-M5","2000","2019","Parliament Mavisi")
audi = Araba("Q7","2000","2019","Lacivert")

class MarvelHero:
    def __init__(self,guc,yetenek,cinsiyet,zayifyon,saglik):
        self.guc = guc
        self.yetenek = yetenek
        self.cinsiyet = cinsiyet
        self.zayifyon = zayifyon
        self.saglik = saglik
    
    def Vurus(self):
        return self.guc

    def Saglik(self,darbe):
        self.saglik -= darbe
        

class Deadpool(MarvelHero):
    def __init__(self):
        super().__init__(200,"yenilenme","Erkek","WHAM",1000)
    
    def Vurus(self):
        return self.guc/2

class Hulk(MarvelHero):
    def __init__(self):
        super().__init__(250,"Yeşil","Erkek","Öfke",2000)
    
    def Saglik(self,darbe):
        self.saglik -= darbe*2




P1 = Hulk()
P2 = Deadpool()


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
    tip = "SUV" # Class Attribute
    arabalar = []   # Class Attribute
    def __init__(self,model="",hp="",yil="",renk=""):
        self.renk = renk  #instance attribute
        self.model = model
        self.hp = hp
        self.yil = yil
        Araba.arabalar.append(model)

    def Gazla(self):  #instance method
        print(self.model,"Gazladı")
    
    def Durdu(self): #instance method
        print(self.model,self.yil,"Durdu")

    @classmethod 
    def tipiSoyle(cls):#class method
        print(cls.tip)

    @classmethod
    def arabaListe(cls): #class method
        print(*cls.arabalar,sep="\n")


mercu = Araba("SLK-200-AMG","2000","2019","Şeytan Kırmızısı")
kuskas = Araba("5.20i-M5","2000","2019","Parliament Mavisi")
kıyyum = Araba("Q7","2000","2019","Lacivert")

mercu.arabaListe()
kuskas.arabaListe()
kıyyum.arabaListe()
Araba.arabaListe()




class MarvelHero:
    def __init__(self,guc,yetenek,cinsiyet,zayifyon,saglik):
        self.guc = guc
        self.yetenek = yetenek
        self.cinsiyet = cinsiyet
        self.zayifyon = zayifyon
        self.saglik = saglik
        print("merhaba")
    
    def Vurus(self):
        return self.guc

    def Saglik(self,darbe):
        self.saglik -= darbe
    
    def __del__(self):
        print("Hoşçakal")
        
class Deadpool(MarvelHero):
    def __init__(self):
        super().__init__(200,"yenilenme","Erkek","WHAM",1000)
        self.__love = "Ayşe"

    def setter(self,sevgili):
        if sevgili == "Ahmet":
            print("Sevgili ismi erkek olamaz")
        else:
            self.__love = sevgili

    def getter(self):
        return self.__love

    def Vurus(self):
        return self.guc/2

class Hulk(MarvelHero,Deadpool):
    def __init__(self):
        super().__init__(250,"Yeşil","Erkek","Öfke",2000)
        self.__gama = True

    @property
    def gama(self):
        return self.__gama
    
    @gama.setter
    def gama(self,val):
        if str(type(val)) == "<class 'bool'>":
            self.__gama = val

    @gama.deleter
    def gama(self):
        print("Haydaaaa niye sildin")
    
    def Saglik(self,darbe):
        self.saglik -= darbe*2

P1 = Deadpool()
print(P1.getter())
P2 = Hulk()
P2.gama = False
print(P2.gama)
del P2.gama


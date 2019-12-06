from random import choice

class MarvelHero:
    __heroList = []
    def __init__(self,guc,saglik,adi,superGuc):
        self.guc = guc
        self.MaxSaglik = saglik
        self.saglik = saglik
        self.adi = adi
        self.superGuc = superGuc
        self.__gucBirikim = 0
        MarvelHero.__heroList.append(self.adi)
    def Vurus(self):
        self.gucBirikim = 1
        return self.guc

    def Vurus2(self):
        self.gucBirikim = 2
        return self.guc*1.25

    def Vurus3(self):
        self.gucBirikim = 2
        return self.guc*2

    def DarbeAl(self,darbe):
        self.saglik -= darbe
    def Savunma(self,darbe):
        print(self.adi,"Savunma Yaptı")
        self.saglik -= darbe//2
    def SuperVurus(self):
        if self.__gucBirikim >= 4:
            self.__gucBirikim = 0
            print(self.adi,"Süper Vuruş Yaptı")
            return self.guc*self.superGuc
        else:
            return self.Vurus()

    def __len__(self):
        return len(MarvelHero.__heroList)

    # def BirikimAyarla(self,deger): # setter
    #     self.__gucBirikim = (self.__gucBirikim + deger )% 5
    
    # def BirikimGetir(self): ## getter
    #     return self.__gucBirikim

    @property
    def gucBirikim(self): ## getter
        return self.__gucBirikim

    @gucBirikim.setter
    def gucBirikim(self,deger):
        self.__gucBirikim = (self.__gucBirikim + deger )% 5

    @gucBirikim.deleter
    def gucBirikim(self):
        self.__gucBirikim = 0
    

    def VurusGetir(self):
        hareket = [self.Vurus,self.Vurus2,self.Vurus3,self.SuperVurus]
        return choice(hareket)

    def DarbeAlGetir(self):
        hareket = [self.DarbeAl,self.Savunma]
        return choice(hareket)



    def Durum(self):
        bar = (self.saglik*100)/self.MaxSaglik
        barPer =bar//10
        return "Durum {} - Sağlık:{}%{}".format(self.adi,
        int(barPer)*"#",round(bar))
    
    def __del__(self):
        print("Hoşçakal")

    def __str__(self):
        return self.adi

###################################
# from abc import ABCMeta,abstractmethod

# class Hero:
#     __metaclass__ = ABCMeta

#     @abstractmethod
#     def killaHakan(self):
#         return "2 2 1 0"

# class Rep(Hero):
#     def killaHakan(self):
#         s = super(Rep,self).killaHakan()
#         return "{}".format(s)

# r = Rep()
# print(r.killaHakan())

################################



    
# P1 = MarvelHero(100,1000,"Deadpool")
        
class Deadpool(MarvelHero):
    def __init__(self):
        super().__init__(100,1000,"Deadpool",2)

    def DarbeAl(self,darbe): #override
        self.saglik -= darbe//2  

class Hulk(MarvelHero):
    def __init__(self):
        super().__init__(100,2000,"Hulk",1.5)
    
    def Vurus(self):
        self.gucBirikim = 1
        return self.guc*2

class IronMan(MarvelHero):
    def __init__(self):
        super().__init__(150,1500,"IronMan",3)

class Tarkan(MarvelHero):
    def __init__(self):
        super().__init__(200,1500,"Tarkan",1.25)

    def DarbeAl(self,darbe):
        self.saglik -= darbe//3

    def Vurus(self):
        self.gucBirikim = 1
        return self.guc//2


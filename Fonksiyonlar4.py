def fonk(a=0,b=[]):
    pass

print("ali",1,2,sep="-")

def fonk2(*args):
    for item in args:
        print(item)

# fonk2("ali",1,2,3,4,5,"veli")

# sozluk = {"1":1,"1":2}

def fonk3(**kwargs):
    for key,value in kwargs.items():
        if key == "Uyhular":
            print(key,value)
        elif key == "Gencligim_bah":
            print(key,value)

fonk3(Uyhular="Haram Oldu",Gencligim_bah="Talan da oldu")
def toplam(a=0,b=0):
    return a+b
def cikarma(a=0,b=0):
    return a-b
def carpma(a=0,b=0):
    return a*b
def bolme(a=0,b=0):
    return a/b
def calistir(fonk,a,b):
    return fonk(a,b)
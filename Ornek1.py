# liste = [1,2,3,4,5]
# liste = liste + [1,2,3]
# print(liste)
# liste.append([4,5])
# print(liste)
# liste.insert(0,0)
# print(liste)
# liste.extend([6,7,8])
# print(liste)
# liste.insert(0,[1,2,3,4])
# print(liste)
alisveris = ["ekmek","peynir","yoğurt","domates"]
alisveris.append("biber")
print("1",alisveris)
alisveris[0] = "pirinç"
print("2",alisveris)
alisveris.remove("peynir")
print("3",alisveris)
print(alisveris.pop(0))
print("4",alisveris)
del alisveris[1]
print("5",alisveris)
alisveris.append("Çiğdem")
print("6",alisveris)
alisveris.sort()
print("7",alisveris)
liste = alisveris.copy()
liste[0] = "zerdeçal"
print("8",alisveris)


metin = "zeki"
metin1 = metin
metin1 = metin1.replace("e","")
print(metin)
















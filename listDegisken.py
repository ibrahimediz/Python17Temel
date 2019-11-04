# liste = [1,2,"deneme",2.0,[1,"aaa"],(2,3.33)]
# print(liste[4][1])
# liste[0] = 7
# liste.append("eklendi")
# print(liste)
# liste.insert(0,"eklendi")
# print(liste)
# len(liste)

liste = [1, 2, 3, 4, 5, 6, 7, 8]
liste.append(9)
print("1", liste)
liste.insert(0, 0)
print("2", liste)
liste.remove(5)
print("3", liste)
print(liste.pop(2))
print("4", liste)
del liste[0]
print("5", liste)

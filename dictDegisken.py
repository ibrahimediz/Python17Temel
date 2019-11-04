sozluk = {
    "kitap":"book",
    "kalem":"pencil",
    "masa":"table"
}
print("1",sozluk["kitap"])
sozluk.update({"glass":"bardak"})
print("2",sozluk)
# sozluk["jamiryo"]
print("3",sozluk.get("kitap"))
print("4",sozluk.keys())
print("5",sozluk.values())
liste = ["ali","veli","hakkı","soner"]
sozluk = dict.fromkeys(liste,"0")
print("6",sozluk)
sozluk["ali"] = 7
print("7",sozluk)
print("8",sozluk.items())
for key,value in sozluk.items():
    print(key,"-",value)
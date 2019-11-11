# 9,228,852
# Dokuz Milyon İki Yüz Yirmi Sekiz Bin Sekiz Yüz Elli İki

var1 = "9,228,852"
var1 =  var1.replace(",","").replace(".","")
print(var1)
while len(var1)%3 != 0:
    var1 = "0" + var1

# for i in range(0,3-len(var1))

# var1[0:3] 009
# var1[3:6]
# var1[6:9]
liste = []
for i in range(int(len(var1)/3)):
    # print(var1[(i*3)+0:(i*3)+3])
    liste.append(var1[(i*3)+0:(i*3)+3])
{"0":"",
"1":"Bir",
"2":}

    
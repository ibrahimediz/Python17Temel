a = 5
def fonk():
    global a
    a = 3
    print(a)
print(a)
fonk()
print(a)
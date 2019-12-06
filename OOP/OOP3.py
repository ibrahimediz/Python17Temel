class A(): #grandparent
    def __init__(self):
        print("A")

    def fonk(self):
        print("A fonk")

class B(A): #parent
    def __init__(self):
        super(B,self).__init__()
        print("B") 

    def fonk(self):
        print("B fonk")

class C(B): #child
    def __init__(self):
        super(C,self).__init__()
        print(f'Square area: {1+1}')



c = C()
c.fonk()
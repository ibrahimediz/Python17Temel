class A():
    def __init__(self):
        print("A")
    
    def fonk(self):
        print("A fonk")

class B(A):
    def __init__(self):
        super().__init__()
        print("B") 

    def fonk(self):
        print("B fonk")

class C(B):
    def __init__(self):
        super().__init__()
        print("C")

c = C()
c.fonk()

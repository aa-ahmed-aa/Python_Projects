class mario():

    def move(self):
        print("i am Moving !! ")

class Mushro():
    def eatMuch(self):
        print("i am big #!#$")


class BigMario(mario, Mushro):
    pass

bm = BigMario()
bm.move()
bm.eatMuch()
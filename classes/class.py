class tuna:
    life = 3

    def attack(self):
        print(" ouch !! ")
        self.life -= 1

    def check(self):
        if self.life <= 0:
            print("iam dead !@@@#@#@#@#!@#@#!@!@$@#")
        else :
            print(self.life , "life lift ")

player = tuna()

player.attack()
player.check()
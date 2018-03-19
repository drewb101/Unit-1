class Cat:

    def __init__(self, n, amtOfHair, voice):

        self.name = n
        self.lives = 9
        self.amtOfHair = amtOfHair
        self.voice = voice
    
    def meow(self):
        print(self.name + "says: " + self.voice)

    def shed(self, howMuch):
        if self.amtOfHair >= howMuch:
            
        self.amtOfHair -= howMuch
    
    def getAmtOfHair(self):
        return self.amtOfHair



franklin = Cat("Franklin ", 40000, "MRRRRRRRRRRRROOOOOOOOOOOOOWWWWWW!!!!!!")
franklin.meow()
print(franklin.getAmtOfHair())
franklin.shed(10000)
print(franklin.getAmtOfHair())
franklin.shed(30000)
print(franklin.getAmtOfHair())
garfield = Cat("Garfield ", 500000, "Where's my lasagna?")
garfield.meow()
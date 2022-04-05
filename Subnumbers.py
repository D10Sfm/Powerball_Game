# The class of the logic draw
from random import *
from Numbers import Numbers


class Subnumbers(Numbers):
    def __init__(self):
        super().__init__(rangeofwhite=21, rangeofgold=11)

    def getwhiteballs(self):
        subcribdnums = []
        x = 0
        while x != 5:
            y = randrange(1, self.getrangeofwhite())
            subcribdnums.append(y)
            x += 1
        return sorted(subcribdnums, reverse=False)

    def getpowerball(self):
        powerball = randrange(1, self.getrangeofgold())
        return powerball

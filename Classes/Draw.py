# The class of the logic draw
from random import *
from Classes.Numbers import Numbers


class Draw(Numbers):      # Creating a class for the drawing of the numbers
    def __init__(self):      # def an constructor from the numbers class
        super().__init__(rangeofwhite=21, rangeofgold=11)    # the numbers class parameters(range)

    def getwhiteballs(self):    # def a function for getting the list of white numbers
        subcribdnums = []      # the empty list
        x = 0        # counter for limit the list to 5 numbers
        while x != 5:
            y = randrange(1, self.getrangeofwhite())     # the random number
            if y not in subcribdnums:
                subcribdnums.append(y)
                x += 1
            else:
                pass
        return sorted(subcribdnums, reverse=False)      # return the list with ascending order

    def getpowerball(self):     # def a function for the powerball
        powerball = randrange(1, self.getrangeofgold())
        return powerball

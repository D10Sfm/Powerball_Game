# Main Static class for the numbers range
import warnings    # import warnings module for printing a warning message

class Numbers:      # creating a main class of numbers (ranges)
    def __init__(self, rangeofwhite=21, rangeofgold=11):       # constructor for the class
        self.rangeofwhite = rangeofwhite
        self.rangeofgold = rangeofgold

    def getrangeofwhite(self):       # get methode for the whiteballs range
        return self.rangeofwhite

    def getrangeofgold(self):        # get methode for the goldball range
        return self.rangeofgold

    def __setrange__(self, rangeof, x):    #  set method for setting new range of draw
        if x == 1:     # x representing the choice of what range you want to change 1=whiteballs 2-goldball
            self.rangeofwhite = rangeof
        elif x == 2:
            self.rangeofgold = rangeof
        else:
            warnings.warn("Wrong Choice!")


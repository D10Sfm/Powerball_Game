# Main Static class for the numbers range
import sys


class Numbers:
    def __init__(self, rangeofwhite=21, rangeofgold=11):
        self.rangeofwhite = rangeofwhite
        self.rangeofgold = rangeofgold

    def getrangeofwhite(self):
        return self.rangeofwhite

    def getrangeofgold(self):
        return self.rangeofgold

    def __setrange__(self, rangeof, x):
        if x == 1:
            self.rangeofwhite = rangeof
        elif x == 2:
            self.rangeofgold = rangeof
        else:
            print(sys.stderr.write("Wrong Choise!!"))

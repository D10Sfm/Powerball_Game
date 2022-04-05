# The Main class of the game her i will execute and combined all the methods
from Subnumbers import Subnumbers
from Functions import *
class Powerball(Subnumbers):

    def powerball(self):
        subcribenum = [self.getwhiteballs(),self.getpowerball()]
        machinenum = [self.getwhiteballs(),self.getpowerball()]
        y = 0
        f = False
        for (i,j) in zip(subcribenum[0],machinenum[0]):
            if i == j:
                y += 1
            else:
                pass
        if subcribenum[1] == machinenum[1]:
            f += True
        else:
            pass
        print(subcribenum,machinenum,sep="\n")
        displayed(y,f)
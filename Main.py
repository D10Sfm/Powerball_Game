# The Main class of the game her i will execute and combined all the methods
from Subnumbers import Subnumbers
from Functions import *


class Powerball(Subnumbers):  # Create the main game class

    def powerball(self):  # Creating the main function of the game
        subcribenum = [self.getwhiteballs(), self.getpowerball()]  # Create a variable for the white ball list and
        # the power ball for the subcribe
        machinenum = [self.getwhiteballs(), self.getpowerball()]  # As above just for the game machine
        y = 0  # Counter for the hits of subscribe
        f = False  # Flag for the Powerball number : False = No hit!,True = Hit!
        for (i, j) in zip(machinenum[0], subcribenum[0]):  # a double loop for two iterators in machine number
            # and subscribe numbers  simultaneously
            if j == i or j in machinenum[0]:
                y += 1
            else:
                pass
        if subcribenum[1] == machinenum[1]:
            f += True
        else:
            pass
        game_draw_printing('| '.join(map(str, machinenum[0])), str(machinenum[1]))   # print the machine game numbers
        # without a bracebrackets
        sub_draw_printing('| '.join(map(str, subcribenum[0])), str(subcribenum[1]))  # print the subscribe numbers
        # without
        # a bracebrackets
        displayed(y, f)

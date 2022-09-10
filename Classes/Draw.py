# The class of the logic draw
from random import *
# from Classes.Numbers import Numbers
from Utilities.Functions import *
import warnings


class Draw:      # Creating a class for the drawing of the numbers
    def __init__(self, rangeofwhite=21, rangeofgold=11):  # constructor for the class
        self.rangeofwhite = rangeofwhite
        self.rangeofgold = rangeofgold    # the numbers class parameters(range)


    def getrangeofwhite(self):       # get methode for the whiteballs range
        return self.rangeofwhite

    def getrangeofgold(self):        # get methode for the goldball range
        return self.rangeofgold

    def __setrange__(self, rangeof, x):    #  set method for setting new range of draw
        if x == 1:     # whiteballs representing the choice of what range you want to change 1=whiteballs 2-goldball
            self.rangeofwhite = rangeof
        elif x == 2:
            self.rangeofgold = rangeof
        else:
            warnings.warn("Wrong Choice!")

    def getwhiteballs(self):    # def a function for getting the list of white numbers
        whiteballs_numbers = set()      # the empty set
        while len(whiteballs_numbers) < 5:
            random_num = randrange(1, self.getrangeofwhite())     # the random number
            whiteballs_numbers.add(random_num)
        return sorted(whiteballs_numbers, reverse=False)      # return the list with ascending order

    def getpowerball(self):     # def a function for the play
        powerball = randrange(1, self.getrangeofgold())
        return powerball

    def get_results(self):
        user_numbers = [self.getwhiteballs(), self.getpowerball()]
        game_numbers = [self.getwhiteballs(), self.getpowerball()]  # As above just for the game machine
        hits_number = 0  # Counter for the hits of subscribe
        powerball_hit = False  # Flag for the Powerball number : False = No hit!,True = Hit!
        for (game_num, user_num) in zip(game_numbers[0],user_numbers[0]):
            if user_num == game_num or user_num in game_numbers[0]:
                hits_number += 1
        if user_numbers[1] == game_numbers[1]:
            powerball_hit = True
        user_white_balls = game_numbers[0]
        user_power_ball = str(game_numbers[1])
        game_white_balls = user_numbers[0]
        game_power_ball = user_numbers[1]
        draw_printing(user_white_balls, user_power_ball, True)
        draw_printing(game_white_balls, game_power_ball, False)
        print(result_display(hits_number, powerball_hit))

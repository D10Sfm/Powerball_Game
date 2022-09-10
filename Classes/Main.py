# The Main class of the game her i will execute and combined all the methods
from Classes.Draw import Draw
from Utilities.Functions import *
import keyboard


class Powerball(Draw):  # Create the main game class

    def play(self):  # Creating the main function of the game
        print('Welcome to play draw!\n------------------------\n')
        print('press any key to start the draw...')
        while True:
            if keyboard.is_pressed('s'):
                break
        self.get_results()

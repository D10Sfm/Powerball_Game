# Function section
import colorama    # import the colorama module for printing a string with color
from colorama import Fore     # import the Fore lib for the color option
from colorama import Style    # import Style lib for the style of the color


def displayed(y, f,):    # def a function for the result of the subscription
    if y == 5:     # y representing the amount of hits of the subscription on the whiteball
        if f:      # f is the flag for the hitting on the powernumber ,f=True=hit on powerball f=False dont hit the
            # powerball
            print(f"{y} Correct White Balls and Powerball: Jackpot"+" "+Fore.YELLOW+"$324,000,000"+Style.RESET_ALL)
        else:
            print(f"{y} Correct White Balls and no Powerball:"+" "+Fore.YELLOW+"$1,000,000"+Style.RESET_ALL)
    elif y == 4:
        if f:
            print(f"{y} Correct White Balls and Powerball:"+" "+Fore.YELLOW+"$10,000"+Style.RESET_ALL)
        else:
            print(f"{y} Correct White Balls and no Powerball:"+" "+Fore.YELLOW+"$100"+Style.RESET_ALL)
    elif y == 3:
        if f:
            print(f"{y} Correct White Balls and Powerball:"+" "+Fore.YELLOW+"$100"+Style.RESET_ALL)
        else:
            print(f"{y} Correct White Balls and no Powerball:"+" "+Fore.YELLOW+"$7"+Style.RESET_ALL)
    elif y == 2:
        if f:
            print(f"{y} Correct White Balls and Powerball:"+" "+Fore.YELLOW+"$7"+Style.RESET_ALL)
        else:
            print(f"{y} Correct White Balls and no Powerball! Please Try again!")
    elif y == 1:
        if f:
            print(f"{y} Correct White Balls and Powerball:"+" "+Fore.YELLOW+"$4"+Style.RESET_ALL)
        else:
            print(f"{y} Correct White Balls and no Powerball! Please Try again!")
    elif y == 0:
        if f:
            print("No White Balls Just Powerball:"+" "+Fore.YELLOW+"$4"+Style.RESET_ALL)
        else:
            print("Try again!")
    elif y > 5:     # An flag for check if the counter loop is correct
        print("Something wrong check numbers")
    else:
        print("Try again!")


def sub_draw_printing(x, y):      # def a function for printing the numbers of subscription
    print("Your Lucky Numbers:")
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + f"{x}" + Style.RESET_ALL, Fore.YELLOW + f"{y}" + Style.RESET_ALL, sep="- ")


def game_draw_printing(x, y):   # def a function for printing the numbers of the game
    colorama.init()
    print("Today Powerball Winning Numbers:")
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + f"{x}" + Style.RESET_ALL, Fore.YELLOW + f"{y}" + Style.RESET_ALL, sep="- ")




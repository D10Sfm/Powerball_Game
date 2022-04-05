# Function section
import colorama
from colorama import Fore
from colorama import Style


def displayed(y, f,):
    if y == 5:
        if f:
            print(f"{y} Correct White Balls and Powerball: Jackpot $324,000,000")
        else:
            print(f"{y} Correct White Balls and no Powerball: $1,000,000")
    elif y == 4:
        if f:
            print(f"{y} Correct White Balls and Powerball: $10,000")
        else:
            print(f"{y} Correct White Balls and no Powerball: $100")
    elif y == 3:
        if f:
            print(f"{y} Correct White Balls and Powerball: $100")
        else:
            print(f"{y} Correct White Balls and no Powerball: $7")
    elif y == 2:
        if f:
            print(f"{y} Correct White Balls and Powerball: $7")
        else:
            print(f"{y} Correct White Balls and no Powerball! Please Try again!")
    elif y == 1:
        if f:
            print(f"{y} Correct White Balls and Powerball: $4")
        else:
            print(f"{y} Correct White Balls and no Powerball! Please Try again!")
    elif y == 0:
        if f:
            print("No White Balls Just Powerball: $4")
        else:
            print("Try again!")
    elif y > 5:
        print("Something wrong check numbers")
    else:
        print("Try again!")


def sub_draw_printing(x, y):
    colorama.init()
    print("Today Powerball Winning Numbers:")
    print(Fore.BLUE + Style.DIM + f"{x}" + Style.RESET_ALL, Fore.YELLOW + f"{y}" + Style.RESET_ALL, sep=" - ")


def game_draw_printing(x, y):
    print("Your Lucky Numbers:")
    print(Fore.BLUE + Style.DIM + f"{x}" + Style.RESET_ALL, Fore.YELLOW + f"{y}" + Style.RESET_ALL, sep=" - ")

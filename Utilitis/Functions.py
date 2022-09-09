# Function section

from colorama import Fore  # import the Fore lib for the color option
from colorama import Style  # import Style lib for the style of the color


def results(prize, hits, win=True):
    if hits > 0 and win:
        return f"{hits} Correct White Balls and Powerball: Jackpot" + " " + money_coloring(prize)
    elif hits <= 0 and win:
        return "No White Balls Just Powerball:" + " " + money_coloring(prize)
    elif hits == 0:
        return "Try again!"
    else:
        return f"{hits} Correct White Balls and no Powerball:" + " " + money_coloring(prize)


def prize_money(x, y):
    prize = ''
    if x == 3 and y or x == 4 and not y:
        prize = "$100"
    elif x == 3 and not y or x == 2 and y:
        prize = "$7"
    elif x == 1 and y or y:
        prize = "$4"
    elif x > 4:
        if y:
            prize = "$324,000,000"
        else:
            prize = "$1,000,000"
    elif x == 4 and y:
        prize = "$10,000"

    return prize


def money_coloring(money):
    return Fore.YELLOW + money + Style.RESET_ALL


def result_display(whiteball_hits, powerball_hit, ):
    prize = prize_money(whiteball_hits, powerball_hit)
    result = results(prize, whiteball_hits, powerball_hit)
    return result


def draw_printing(whiteballs, powerball, id):  # def a function for printing the numbers of the game
    if id:
        print("Your Lucky Numbers:")
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + f"{result_output(whiteballs)}" + Style.RESET_ALL,
              Fore.YELLOW + f"{powerball}" + Style.RESET_ALL, sep="- ")
    else:
        print("Today Powerball Winning Numbers:")
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + f"{result_output(whiteballs)}" + Style.RESET_ALL,
              Fore.YELLOW + f"{powerball}" + Style.RESET_ALL, sep="- ")


def result_output(result):
    return '| '.join(map(str, result))

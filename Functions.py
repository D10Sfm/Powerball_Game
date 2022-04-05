def displayed(y, f):
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
    else:
        print("Try again!")

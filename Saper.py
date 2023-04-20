import random
#(xtoguess + 6 * ytoguess) -> the value to use with bombplacement variable to check for bombs
#theboard[5 - ytoguess][xtoguess] -> the value to use to acces the location on the board of a guessed file

theboard = [["x" for number in range(6)], ["x" for number in range(6)], ["x" for number in range(6)],
            ["x" for number in range(6)], ["x" for number in range(6)], ["x" for number in range(6)]]


checkedlocations = []
bombplacement = []


def numberofbombs():
    while True:
        nbombs = input("How many bombs?\n You can pick up to 35 bombs. \nFloating numbers will be rounded down.\n")
        try:
            nbombs = int(nbombs)
            if nbombs > 35 or nbombs < 1:
                print("Invalid amount of bombs! Pick again!")
                continue
            break
        except ValueError:
            print("Invalid amount of bombs! Pick again!")
            continue
    return nbombs


def bombplacementfunc(nbombs):
    return random.sample(range(35), nbombs, counts=None)


def areyawinningson():
    for row in theboard:
        for i in range(6):
            if row[i] == "x":
                return 0
    for bomb in bombplacement:
        if not theboard[5-int(bomb/6)][bomb//6] == "m":
            return 0
        else:
            print("You won")
            exit()


def valueassessment(ytoguess, xtoguess):
    if (ytoguess, xtoguess) not in checkedlocations:
        checkedlocations.append((ytoguess, xtoguess))
        if (xtoguess + 6 * ytoguess) == 0:
            bombsinvicinity = 0
            if (xtoguess + 6 * ytoguess + 6) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess + 7) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess + 1) in bombplacement:
                bombsinvicinity += 1
            theboard[5 - ytoguess][xtoguess] = str(bombsinvicinity)
            if bombsinvicinity == 0:
                if (ytoguess + 1, xtoguess + 1) not in checkedlocations:
                    valueassessment(ytoguess + 1, xtoguess + 1)
                if (ytoguess + 1, xtoguess) not in checkedlocations:
                    valueassessment(ytoguess + 1, xtoguess)
                if (ytoguess, xtoguess + 1) not in checkedlocations:
                    valueassessment(ytoguess, xtoguess + 1)
        elif (xtoguess + 6 * ytoguess) == 5:
            bombsinvicinity = 0
            if (xtoguess + 6 * ytoguess + 6) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess + 5) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess - 1) in bombplacement:
                bombsinvicinity += 1
            theboard[5 - ytoguess][xtoguess] = str(bombsinvicinity)
            if bombsinvicinity == 0:
                if (ytoguess, xtoguess - 1) not in checkedlocations:
                    valueassessment(ytoguess, xtoguess - 1)
                if (ytoguess + 1, xtoguess - 1) not in checkedlocations:
                    valueassessment(ytoguess + 1, xtoguess - 1)
                if (ytoguess + 1, xtoguess) not in checkedlocations:
                    valueassessment(ytoguess + 1, xtoguess)
        elif (xtoguess + 6 * ytoguess) == 30:
            bombsinvicinity = 0
            if (xtoguess + 6 * ytoguess + 1) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess - 6) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess - 5) in bombplacement:
                bombsinvicinity += 1
            theboard[5 - ytoguess][xtoguess] = str(bombsinvicinity)
            if bombsinvicinity == 0:
                if (ytoguess, xtoguess + 1) not in checkedlocations:
                    valueassessment(ytoguess, xtoguess + 1)
                if (ytoguess - 1, xtoguess) not in checkedlocations:
                    valueassessment(ytoguess - 1, xtoguess)
                if (ytoguess - 1, xtoguess + 1) not in checkedlocations:
                    valueassessment(ytoguess - 1, xtoguess + 1)
        elif (xtoguess + 6 * ytoguess) == 35:
            bombsinvicinity = 0
            if (xtoguess + 6 * ytoguess - 6) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess - 7) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess - 1) in bombplacement:
                bombsinvicinity += 1
            theboard[5 - ytoguess][xtoguess] = str(bombsinvicinity)
            if bombsinvicinity == 0:
                if (ytoguess - 1, xtoguess) not in checkedlocations:
                    valueassessment(ytoguess - 1, xtoguess)
                if (ytoguess - 1, xtoguess - 1) not in checkedlocations:
                    valueassessment(ytoguess - 1, xtoguess - 1)
                if (ytoguess, xtoguess - 1) not in checkedlocations:
                    valueassessment(ytoguess, xtoguess - 1)
        elif (xtoguess + 6 * ytoguess) == 31 or (xtoguess + 6 * ytoguess) == 32 or (xtoguess + 6 * ytoguess) == 33 or (
                xtoguess + 6 * ytoguess) == 34:
            bombsinvicinity = 0
            if (xtoguess + 6 * ytoguess - 1) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess - 7) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess - 6) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess - 5) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess + 1) in bombplacement:
                bombsinvicinity += 1
            theboard[5 - ytoguess][xtoguess] = str(bombsinvicinity)
            if bombsinvicinity == 0:
                if (ytoguess, xtoguess - 1) not in checkedlocations:
                    valueassessment(ytoguess, xtoguess - 1)
                if (ytoguess - 1, xtoguess - 1) not in checkedlocations:
                    valueassessment(ytoguess - 1, xtoguess - 1)
                if (ytoguess - 1, xtoguess) not in checkedlocations:
                    valueassessment(ytoguess - 1, xtoguess)
                if (ytoguess - 1, xtoguess + 1) not in checkedlocations:
                    valueassessment(ytoguess - 1, xtoguess + 1)
                if (ytoguess, xtoguess + 1) not in checkedlocations:
                    valueassessment(ytoguess, xtoguess + 1)
        elif (xtoguess + 6 * ytoguess) == 24 or (xtoguess + 6 * ytoguess) == 18 or (xtoguess + 6 * ytoguess) == 12 or (
                xtoguess + 6 * ytoguess) == 6:
            bombsinvicinity = 0
            if (xtoguess + 6 * ytoguess + 6) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess + 7) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess + 1) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess - 5) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess - 6) in bombplacement:
                bombsinvicinity += 1
            theboard[5 - ytoguess][xtoguess] = str(bombsinvicinity)
            if bombsinvicinity == 0:
                if (ytoguess + 1, xtoguess) not in checkedlocations:
                    valueassessment(ytoguess + 1, xtoguess)
                if (ytoguess + 1, xtoguess + 1) not in checkedlocations:
                    valueassessment(ytoguess + 1, xtoguess + 1)
                if (ytoguess, xtoguess + 1) not in checkedlocations:
                    valueassessment(ytoguess, xtoguess + 1)
                if (ytoguess - 1, xtoguess + 1) not in checkedlocations:
                    valueassessment(ytoguess - 1, xtoguess + 1)
                if (ytoguess - 1, xtoguess) not in checkedlocations:
                    valueassessment(ytoguess - 1, xtoguess)
        elif (xtoguess + 6 * ytoguess) == 1 or (xtoguess + 6 * ytoguess) == 2 or (xtoguess + 6 * ytoguess) == 3 or (
                xtoguess + 6 * ytoguess) == 4:
            bombsinvicinity = 0
            if (xtoguess + 6 * ytoguess - 1) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess + 5) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess + 6) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess + 7) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess + 1) in bombplacement:
                bombsinvicinity += 1
            theboard[5 - ytoguess][xtoguess] = str(bombsinvicinity)
            if bombsinvicinity == 0:
                if (ytoguess, xtoguess - 1) not in checkedlocations:
                    valueassessment(ytoguess, xtoguess - 1)
                if (ytoguess + 1, xtoguess - 1) not in checkedlocations:
                    valueassessment(ytoguess + 1, xtoguess - 1)
                if (ytoguess + 1, xtoguess) not in checkedlocations:
                    valueassessment(ytoguess + 1, xtoguess)
                if (ytoguess + 1, xtoguess + 1) not in checkedlocations:
                    valueassessment(ytoguess + 1, xtoguess + 1)
                if (ytoguess, xtoguess + 1) not in checkedlocations:
                    valueassessment(ytoguess, xtoguess + 1)
        elif (xtoguess + 6 * ytoguess) == 29 or (xtoguess + 6 * ytoguess) == 23 or (xtoguess + 6 * ytoguess) == 17 or (
                xtoguess + 6 * ytoguess) == 11:
            bombsinvicinity = 0
            if (xtoguess + 6 * ytoguess + 6) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess + 5) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess - 1) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess - 7) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess - 6) in bombplacement:
                bombsinvicinity += 1
            theboard[5 - ytoguess][xtoguess] = str(bombsinvicinity)
            if bombsinvicinity == 0:
                if (ytoguess + 1, xtoguess) not in checkedlocations:
                    valueassessment(ytoguess + 1, xtoguess)
                if (ytoguess + 1, xtoguess - 1) not in checkedlocations:
                    valueassessment(ytoguess + 1, xtoguess - 1)
                if (ytoguess, xtoguess - 1) not in checkedlocations:
                    valueassessment(ytoguess, xtoguess - 1)
                if (ytoguess - 1, xtoguess - 1) not in checkedlocations:
                    valueassessment(ytoguess - 1, xtoguess - 1)
                if (ytoguess - 1, xtoguess) not in checkedlocations:
                    valueassessment(ytoguess - 1, xtoguess)
        else:
            bombsinvicinity = 0
            if (xtoguess + 6 * ytoguess + 6) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess + 7) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess + 1) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess - 5) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess - 6) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess + 5) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess - 1) in bombplacement:
                bombsinvicinity += 1
            if (xtoguess + 6 * ytoguess - 7) in bombplacement:
                bombsinvicinity += 1
            theboard[5 - ytoguess][xtoguess] = str(bombsinvicinity)
            if bombsinvicinity == 0:
                if (ytoguess + 1, xtoguess) not in checkedlocations:
                    valueassessment(ytoguess + 1, xtoguess)
                if (ytoguess + 1, xtoguess + 1) not in checkedlocations:
                    valueassessment(ytoguess + 1, xtoguess + 1)
                if (ytoguess, xtoguess + 1) not in checkedlocations:
                    valueassessment(ytoguess, xtoguess + 1)
                if (ytoguess - 1, xtoguess + 1) not in checkedlocations:
                    valueassessment(ytoguess - 1, xtoguess + 1)
                if (ytoguess + 1, xtoguess - 1) not in checkedlocations:
                    valueassessment(ytoguess + 1, xtoguess - 1)
                if (ytoguess, xtoguess - 1) not in checkedlocations:
                    valueassessment(ytoguess, xtoguess - 1)
                if (ytoguess - 1, xtoguess - 1) not in checkedlocations:
                    valueassessment(ytoguess - 1, xtoguess - 1)
                if (ytoguess - 1, xtoguess) not in checkedlocations:
                    valueassessment(ytoguess - 1, xtoguess)


def boardappears(theboard):
    for row in theboard:
        print(row)


def guessingormarking():
    while True:
        markorguess = input("Would you like to mark a file, take a guess or exit the game?\nType m, t or e.\n")
        if markorguess != 'm' and markorguess != "t" and markorguess != 'e':
            print("Invalid value! Pick again!")
        elif markorguess == 'm':
            marking()
            areyawinningson()
        elif markorguess == 't':
            guessing()
            areyawinningson()
        elif markorguess == 'e':
            exit()


def guessing():
    while True:
        try:
            print("Guessing an already marked file will be ignored")
            xtoguess = int(input("Select an x coordinate you would like to guess:\n"))
            if xtoguess > 5 or xtoguess < 0:
                print("Invalid value! Pick again!")
                continue
            ytoguess = int(input("Select an y coordinate you would like to guess:\n"))
            if ytoguess > 5 or ytoguess < 0:
                print("Invalid value! Pick again!")
                continue
            else:
                if (xtoguess + 6 * ytoguess) in bombplacement:
                    theboard[5 - ytoguess][xtoguess] = 'b'
                    print('You lost!')
                    boardappears(theboard)
                    exit()
                valueassessment(ytoguess, xtoguess)
                boardappears(theboard)
                break
        except ValueError:
            print("Incorrect value! Pick again!")
            continue


def marking():
    while True:
        print("Marking an already marked file will unmark it.")
        try:
            xtomark= int(input("Select an x coordinate you would like to mark:\n"))
            if xtomark > 5 or xtomark < 0:
                print("Invalid value! Pick again!")
                continue
            ytomark=int(input("Select an y coordinate you would like to mark:\n"))
            if ytomark > 5 or xtomark < 0:
                print("Invalid value! Pick again!")
                continue
            else:
                break
        except ValueError:
            print("Incorrect value! Pick again!")
            continue
    if theboard[5 - ytomark][xtomark] == "m":
        theboard[5 - ytomark][xtomark] = "x"
        checkedlocations.remove((ytomark, xtomark))
    if theboard[5 - ytomark][xtomark].isdigit():
        pass
    else:
        theboard[5 - ytomark][xtomark] = "m"
        checkedlocations.append((ytomark, xtomark))
    boardappears(theboard)


while True:
    print("You will be playing saper.\n Make sure to clear the whole area without getting blown up.\n"
          "The area consists of 6 rows and 6 columns.\n "
          "They are numbered 0-5.\n"
          "Rows from bottom to top.\n"
          "Columns from left to right.\n"
          "The area is presented undearneath this text.\n"
          "You can either mark or guess whether there is a bomb in a selected file.\n")
    bombplacement = bombplacementfunc(numberofbombs())
    boardappears(theboard)
    guessingormarking()

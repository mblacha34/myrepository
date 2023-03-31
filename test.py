theboard = [["x" for number in range(6)], ["x" for number in range(6)], ["x" for number in range(6)],
["x" for number in range(6)], ["x" for number in range(6)], ["x" for number in range(6)]]

bombplacement = [1, 6, 8]


def valueassessment(ytoguess,xtoguess):
    if (xtoguess + 6 * ytoguess) == 0:
        bombsinvicinity=0
        if (xtoguess + 6 * ytoguess + 6) in bombplacement:
            bombsinvicinity += 1
        if (xtoguess + 6 * ytoguess + 7) in bombplacement:
            bombsinvicinity += 1
        if (xtoguess + 6 * ytoguess + 1) in bombplacement:
            bombsinvicinity +=1
        theboard[5 - ytoguess][xtoguess] = str(bombsinvicinity)
        if bombsinvicinity == 0:
            valueassessment(xtoguess + 7, ytoguess)
            valueassessment(xtoguess + 6, ytoguess)
            valueassessment(xtoguess + 1, ytoguess)
        theboard[5 - ytoguess][xtoguess] = str(bombsinvicinity)
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
            valueassessment(xtoguess - 1, ytoguess)
            valueassessment(xtoguess + 5, ytoguess)
            valueassessment(xtoguess + 6, ytoguess)
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
            valueassessment(xtoguess + 1, ytoguess)
            valueassessment(xtoguess - 6, ytoguess)
            valueassessment(xtoguess - 5, ytoguess)
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
            valueassessment(xtoguess - 6, ytoguess)
            valueassessment(xtoguess - 7, ytoguess)
            valueassessment(xtoguess - 1, ytoguess)
    elif (xtoguess + 6 * ytoguess) == 31 or (xtoguess + 6 * ytoguess) == 32 or (xtoguess + 6 * ytoguess) == 33 or (xtoguess + 6 * ytoguess) == 34:
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
            valueassessment(xtoguess - 1, ytoguess)
            valueassessment(xtoguess - 7, ytoguess)
            valueassessment(xtoguess - 6, ytoguess)
            valueassessment(xtoguess - 5, ytoguess)
            valueassessment(xtoguess + 1, ytoguess)
    elif (xtoguess + 6 * ytoguess) == 24 or (xtoguess + 6 * ytoguess) == 18 or (xtoguess + 6 * ytoguess) == 12 or (xtoguess + 6 * ytoguess) == 6:
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
            valueassessment(xtoguess + 6, ytoguess)
            valueassessment(xtoguess + 7, ytoguess)
            valueassessment(xtoguess + 1, ytoguess)
            valueassessment(xtoguess - 5, ytoguess)
            valueassessment(xtoguess - 6, ytoguess)
    elif (xtoguess + 6 * ytoguess) == 1 or (xtoguess + 6 * ytoguess) == 2 or (xtoguess + 6 * ytoguess) == 3 or (xtoguess + 6 * ytoguess) == 4:
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
            valueassessment(xtoguess - 1, ytoguess)
            valueassessment(xtoguess + 5, ytoguess)
            valueassessment(xtoguess + 6, ytoguess)
            valueassessment(xtoguess + 7, ytoguess)
            valueassessment(xtoguess + 1, ytoguess)
    elif (xtoguess + 6 * ytoguess) == 29 or (xtoguess + 6 * ytoguess) == 23 or (xtoguess + 6 * ytoguess) == 17 or (xtoguess + 6 * ytoguess) == 11:
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
            valueassessment(xtoguess + 6, ytoguess)
            valueassessment(xtoguess + 5, ytoguess)
            valueassessment(xtoguess - 1, ytoguess)
            valueassessment(xtoguess - 7, ytoguess)
            valueassessment(xtoguess - 6, ytoguess)
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
            valueassessment(xtoguess + 6, ytoguess)
            valueassessment(xtoguess + 7, ytoguess)
            valueassessment(xtoguess + 1, ytoguess)
            valueassessment(xtoguess - 5, ytoguess)
            valueassessment(xtoguess + 5, ytoguess)
            valueassessment(xtoguess - 1, ytoguess)
            valueassessment(xtoguess - 7, ytoguess)
            valueassessment(xtoguess - 6, ytoguess)
def guessing():
    while True:
        try:
            xtoguess= int(input("Select an x coordinate you would like to guess\n"))
            if xtoguess > 5 or xtoguess < 0:
                print("Invalid value! Pick again!")
                continue
            ytoguess=int(input("Select an y coordinate you would like to guess\n"))
            if ytoguess > 5 or ytoguess < 0:
                print("Invalid value! Pick again!")
                continue
            else:
                if (xtoguess + 6 * ytoguess) in bombplacement:
                    theboard[5 - ytoguess][xtoguess] = 'b'
                    for i in theboard:
                        print(i)
                    print('You lost!')
                    exit()
                valueassessment(ytoguess, xtoguess)
        except ValueError:
            print("Incorrect value! Pick again!")
            continue
        for i in theboard:
            print(i)
guessing()
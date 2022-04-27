# Made by SoonOOv#2199

from re import findall
from math import floor
from numpy import transpose
from random import randint
from os import system

base = " 1 | 2 | 3 \n--- --- ---\n 4 | 5 | 6 \n--- --- ---\n 7 | 8 | 9"

def PVPM():
    global base
    completed = False
    turn = True
    option = findall(r"\d+",base)
    gameCondition = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
    system("clear")
    print(base+"\n")
    while True:
        transposed = transpose(gameCondition).tolist()
        if gameCondition[0][0] == gameCondition[1][1] == gameCondition[2][2]:
            print("Player 1 ( X ) won!") if gameCondition[0][0] == "X" else print("Player 2 ( O ) won!")
            break
        elif gameCondition[0][2] == gameCondition[1][1] == gameCondition[2][0]:
            print("Player 1 ( X ) won!") if gameCondition[0][2] == "X" else print("Player 2 ( O ) won!")
            break
        elif len(option) == 0:
            print("Draw!")
            break
        for i in range(0,3):
            if gameCondition[i].count(gameCondition[i][0]) == len(gameCondition[i]):
                print("Player 1 ( X ) won!") if gameCondition[i][0] == "X" else print("Player 2 ( O ) won!")
                completed = True
            elif transposed[i].count(transposed[i][0]) == len(transposed[i]):
                print("Player 1 ( X ) won!") if transposed[i][0] == "X" else print("Player 2 ( O ) won!")
                completed = True
        if completed:
            break
        if turn:
            pick = input("Player 1's turn, pick a square to mark! " + "Option : " + ", ".join(option) + "\n")
            if pick in base and pick.isdigit():
                option.remove(pick)
                gameCondition[floor(int(pick)/3-0.1) ][int(pick)%3 - 1 if int(pick)%3 - 1 >= 0 else 2 ] = "X"
                base = base.replace(pick,"X")
                turn = False
                system("clear")
                print(base)
            else:
                print(pick+" is either a invalid or already taken!")
        else:
            pick = input("Player 2's turn, pick a square to mark! " + "Option : " + ", ".join(option) + "\n")
            if pick in base and pick.isdigit():
                option.remove(pick)
                gameCondition[floor(int(pick)/3-0.1) ][int(pick)%3 - 1 if int(pick)%3 - 1 >= 0 else 2 ] = "O"
                base = base.replace(pick,"O")
                turn = True
                system("clear")
                print(base)
            else:
                print(pick+" is either a invalid or already taken!")

def PVCM():
    global base
    completed = False
    turn = True if input("Do you want to go first? (y if yes, anything else if no)\n") == "y" else False 
    option = findall(r"\d+",base)
    dif = input("Difficulty : Hard or Normal?\n").lower()
    if not dif == "hard":
        if not dif == "normal":
            print("Invalid input!")
            PVCM()
            return
        
    gameCondition = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
    def bot(x):
        if x == "normal":
            return option[randint(0,len(option) - 1)]
        else:
            if "5" in option:
                return "5"
            transposed = transpose(gameCondition).tolist()
            for i in range(0,3):
                if gameCondition[i].count("O") == 2 and not "X" in gameCondition[i]:
                    arr = gameCondition[i].copy()
                    while "O" in arr:
                        arr.remove("O")
                    return str(arr[0])
                elif transposed[i].count("O") == 2 and not "X" in transposed[i]:
                    arr = transposed[i].copy()
                    while "O" in arr:
                        arr.remove("O")
                    return str(arr[0])
            for i in range(0,3):
                if gameCondition[i].count("X") == 2 and not "O" in gameCondition[i]:
                    arr = gameCondition[i].copy()
                    while "X" in arr:
                        arr.remove("X")
                    return str(arr[0])
                elif transposed[i].count("X") == 2 and not "O" in transposed[i]:
                    arr = transposed[i].copy()
                    while "X" in arr:
                        arr.remove("X")
                    return str(arr[0])
            if gameCondition[0][0] == gameCondition[1][1] and str(gameCondition[2][2]).isdigit():
                return str(gameCondition[2][2])
            elif gameCondition[2][2] == gameCondition[1][1] and str(gameCondition[0][0]).isdigit():
                return str(gameCondition[0][0])
            elif gameCondition[0][2] == gameCondition[1][1] and str(gameCondition[2][0]).isdigit():
                return str(gameCondition[2][0])
            elif gameCondition[2][0] == gameCondition[1][1] and str(gameCondition[0][2]).isdigit():
                return str(gameCondition[0][2])
            elif (gameCondition[0][0] == gameCondition[2][2] or gameCondition[0][2] == gameCondition[2][0]) and len([v for v in option if int(v)%2 == 0]) == 4 :
                return "2"
            elif len([v for v in option if int(v)%2 == 0]) == 3 and len([v for v in option if int(v)%2 == 0]) == 3:
                if gameCondition[1][0] == "X" or gameCondition[1][2] == "X":
                    return "2"
                elif gameCondition[0][1] == "X" or gameCondition[2][1] == "X":
                    return "6"
            copy = [v for v in option if not int(v)%2 == 0]
            if not len(copy) == 0:
                return copy[randint(0,len(copy) - 1)]
            else:
                return option[randint(0,len(option) - 1)]
    system("clear")
    print(base)
    while True:
        transposed = transpose(gameCondition).tolist()
        if gameCondition[0][0] == gameCondition[1][1] == gameCondition[2][2]:
            print("Player ( X ) won!") if gameCondition[0][0] == "X" else print("Computer ( O ) won!")
            break
        elif gameCondition[0][2] == gameCondition[1][1] == gameCondition[2][0]:
            print("Player ( X ) won!") if gameCondition[0][2] == "X" else print("Computer ( O ) won!")
            break
        elif len(option) == 0:
            print("Draw!")
            break
        for i in range(0,3):
            if gameCondition[i].count(gameCondition[i][0]) == len(gameCondition[i]):
                print("Player ( X ) won!") if gameCondition[i][0] == "X" else print("Computer ( O ) won!")
                completed = True
            elif transposed[i].count(transposed[i][0]) == len(transposed[i]):
                print("Player ( X ) won!") if transposed[i][0] == "X" else print("Computer ( O ) won!")
                completed = True
        if completed:
            break
        if turn:
            pick = input("Player's turn, pick a square to mark! " + "Option : " + ", ".join(option) + "\n")
            if pick in base and pick.isdigit():
                option.remove(pick)
                gameCondition[floor(int(pick)/3-0.1) ][int(pick)%3 - 1 if int(pick)%3 - 1 >= 0 else 2 ] = "X"
                base = base.replace(pick,"X")
                turn = False
                system("clear")
                print(base)
            else:
                print(pick+" is either a invalid or already taken!")
        else:
                pick = bot(dif)
                option.remove(pick)
                gameCondition[floor(int(pick)/3-0.1) ][int(pick)%3 - 1 if int(pick)%3 - 1 >= 0 else 2 ] = "O"
                base = base.replace(pick,"O")
                turn = True
                system("clear")
                print(base)
def getGameMode(x):
    gameMode = {
        "PVP": PVPM,
        "PVC": PVCM
    }
    return gameMode.get(x)
def start():
    selection = input("Choose a game mode : PVP, PVC\n").upper()
    if getGameMode(selection):
        getGameMode(selection)()
    else:
        print("Invalid option!")
        start()
start()

from mathGame import mathGame
from store import enter_store
import login

def mainMenu():
    print('')
    login.print_equals()
    print('')

    value = 0

    while(True):
        try:
            print('')
            print('\033[1m' + "*** GAME MAIN MENU ***" + '\033[0m')
            print("1. Play Game")
            print("2. Go to Shop")
            print("3. Visit Profile")
            print("4. Exit to Login Page")

            if(value != 0):
                print('')
                login.print_equals()
                print('')
            choice = int(input("Please enter the numbered option: "))
            value = 1

            if(choice > 5 or choice < 1):
                raise ValueError

        except ValueError:
            print('\033[1m' + "*** PLEASE ENTER A NUMBER 1-5 ***" + '\033[0m')
            value = 0

def additionScene(total_coins):
    while True:
        try:
            difficultyOperation = int(input("1. Easy\n2. Medium\n3. Hard\n4. Return to Operations Menu\n"))
            if difficultyOperation < 1 or difficultyOperation > 4:
                raise ValueError("Error: enter a number between 1-4.")
            elif difficultyOperation == 1:
                total_coins += mathGame("add", "easy").problem()
            elif difficultyOperation == 2:
                total_coins += mathGame("add", "medium").problem()
            elif difficultyOperation == 3:
                total_coins += mathGame("add", "hard").problem()
            elif difficultyOperation == 4:
                break
        except Exception as e:
            print(e)
    return total_coins

def subtractionScene(total_coins):
    while True:
        try:
            difficultyOperation = int(input("1. Easy\n2. Medium\n3. Hard\n4. Return to Operations Menu\n"))
            if difficultyOperation < 1 or difficultyOperation > 4:
                raise ValueError("Error: enter a number between 1-4.")
            elif difficultyOperation == 1:
                total_coins += mathGame("sub", "easy").problem()
            elif difficultyOperation == 2:
                total_coins += mathGame("sub", "medium").problem()
            elif difficultyOperation == 3:
                total_coins += mathGame("sub", "hard").problem()
            elif difficultyOperation == 4:
                break
        except Exception as e:
            print(e)
    return total_coins

def multiplicationScene(total_coins):
    while True:
        try:
            difficultyOperation = int(input("1. Easy\n2. Medium\n3. Hard\n4. Return to Operations Menu\n"))
            if difficultyOperation < 1 or difficultyOperation > 4:
                raise ValueError("Error: enter a number between 1-4.")
            elif difficultyOperation == 1:
                total_coins += mathGame("mul", "easy").problem()
            elif difficultyOperation == 2:
                total_coins += mathGame("mul", "medium").problem()
            elif difficultyOperation == 3:
                total_coins += mathGame("mul", "hard").problem()
            elif difficultyOperation == 4:
                break
        except Exception as e:
            print(e)
    return total_coins

def startScene():
    total_coins = 0
    while True:
        try:
            print(f"\nTotal Coins: {total_coins}")
            operationOption = int(input("1. Add\n2. Sub\n3. Mul\n4. Store\n5. Quit\n"))
            if operationOption < 1 or operationOption > 5:
                raise ValueError("Error: enter a number between 1-5.\n")
            elif operationOption == 1:
                total_coins = additionScene(total_coins)
            elif operationOption == 2:
                total_coins = subtractionScene(total_coins)
            elif operationOption == 3:
                total_coins = multiplicationScene(total_coins)
            elif operationOption == 4:
                total_coins = enter_store(total_coins)
            elif operationOption == 5:
                break
        except Exception as e:
            print(e)

startScene()

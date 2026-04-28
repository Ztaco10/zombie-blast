from mathGame import mathGame
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
            choice = int(input("Please choose a number from"))
            value = 1
            
            if(choice > 5 or choice < 1):
                raise ValueError

        except ValueError:
            print('\033[1m' + "*** PLEASE ENTER A NUMBER 1-5 ***" + '\033[0m')
            value = 0

def additionScene():
    while True:
        try:
            difficultyOperation = int(input("1. Easy\n2. Medium\n3. Hard\n4. Return to Operations Menu\n"))
            if difficultyOperation < 1 or difficultyOperation > 4:
                raise ValueError("Error: enter a number between 1-4.")
            elif difficultyOperation == 1:
                addition = mathGame("add", "easy")
                addition.problem()
            elif difficultyOperation == 2:
                addition = mathGame("add", "medium")
                addition.problem()
            elif difficultyOperation == 3:
                addition = mathGame("add", "hard")
                addition.problem()
            elif difficultyOperation == 4:
                break
        except Exception as e:
            print(e)

def subtractionScene():
    while True:
        try:
            difficultyOperation = int(input("1. Easy\n2. Medium\n3. Hard\n4. Return to Operations Menu\n"))
            if difficultyOperation < 1 or difficultyOperation > 4:
                raise ValueError("Error: enter a number between 1-4.")
            elif difficultyOperation == 1:
                sub = mathGame("sub", "easy")
                sub.problem()
            elif difficultyOperation == 2:
                sub = mathGame("sub", "medium")
                sub.problem()
            elif difficultyOperation == 3:
                sub = mathGame("sub", "hard")
                sub.problem()
            elif difficultyOperation == 4:
                break
        except Exception as e:
            print(e)

def multiplicationScene():
    while True:
        try:
            difficultyOperation = int(input("1. Easy\n2. Medium\n3. Hard\n4. Return to Operations Menu\n"))
            if difficultyOperation < 1 or difficultyOperation > 4:
                raise ValueError("Error: enter a number between 1-4.")
            elif difficultyOperation == 1:
                mul = mathGame("mul", "easy")
                mul.problem()
            elif difficultyOperation == 2:
                mul = mathGame("mul", "medium")
                mul.problem()
            elif difficultyOperation == 3:
                mul = mathGame("mul", "hard")
                mul.problem()
            elif difficultyOperation == 4:
                break
        except Exception as e:
            print(e)

def startScene():
    while True:
        try:
            operationOption = int(input(("1. Add\n2. Sub\n3. Mul\n4. Quit\n")))
            if operationOption < 1 or operationOption > 4:
                raise ValueError("Error: enter a number between 1-4.\n")
            elif operationOption == 1:
                additionScene()
            elif operationOption == 2:
                subtractionScene()
            elif operationOption == 3:
                multiplicationScene()
            elif operationOption == 4:
                break
        except Exception as e:
            print(e)
        

startScene()
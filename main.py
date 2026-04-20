import mathGame
import login

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
        except Exception as e:
            print(e)
                

def subtractionScene():
    difficultyOperation = int(input("1. Easy\n2. Medium\n3. Hard\n4. Return to Operations Menu\n"))
def multiplicationScene():
    difficultyOperation = int(input("1. Easy\n2. Medium\n3. Hard\n4. Return to Operations Menu\n"))

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
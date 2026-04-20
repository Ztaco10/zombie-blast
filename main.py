import mathGame
import login

def startScene():
    while True:
        try:
            operationOption = int(input(("1. Add\n2. Sub\n3. Mul\n4. Quit\n")))
            if operationOption < 1 or operationOption > 4:
                raise ValueError("Error: enter a number between 1-4.\n")
            elif operationOption == 1:
                additionScene():
            elif operationOption == 2:
                subtractionScene():
            elif operationOption == 3:
                multiplicationScene():
            elif operationOption == 4:
                break
        except Exception as e:
            print(e)
        


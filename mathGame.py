# im deciding to create a class to handle
# lives, correctness, etc all in one place
import random

class mathGame():
    def __init__(self, operation, difficulty, lives):
        self.operation = operation
        self.difficulty = difficulty
        self.lives = lives
        self.coins = 0
        self.incorrect = 0
        self.correct = 0
        self.loop = 3
        self.opSign = "+"

    def generateNum(self, difficulty):
        if difficulty == "easy":
            num1 = random.randint(0,9)
            num2 = random.randint(0,9)
        elif difficulty == "medium":
            num1 = random.randint(10,99)
            num2 = random.randint(10,99)
        elif difficulty == "hard":
            num1 = random.randint(10,99)
            num2 = random.randint(99,999)
        numbers = num1, num2
        return numbers

    def problem(self, operation, difficulty):
        if operation == "add":
            while self.loop != 0:
                num1,num2 = self.generateNum(difficulty)
                sol = num1+num2
                try:
                    userAnswer = int(input(f"{num1} + {num2} = "))
                except ValueError as e:
                    print("Error: enter a valid integer\n")
                else:
                    if userAnswer==sol:
                        print("Correct!\n")
                        self.correct += 1
                        self.loop -= 1
                    elif userAnswer!=sol:
                        print("Incorrect, try again.\n")
                        self.incorrect += 1

        if operation == "sub":
            while self.loop != 0:
                num1,num2 = self.generateNum(difficulty)
                sol = num1-num2
                try:
                    userAnswer = int(input(f"{num1} - {num2} = "))
                except ValueError as e:
                    print("Error: enter a valid integer\n")
                else:
                    if userAnswer==sol:
                        print("Correct!\n")
                        self.correct += 1
                        self.loop -= 1
                    elif userAnswer!=sol:
                        print("Incorrect, try again.\n")
                        self.incorrect += 1
        if operation == "mul":
            while self.loop != 0:
                num1,num2 = self.generateNum(difficulty)
                sol = num1*num2
                try:
                    userAnswer = int(input(f"{num1} * {num2} = "))
                except ValueError as e:
                    print("Error: enter a valid integer\n")
                else:
                    if userAnswer==sol:
                        print("Correct!\n")
                        self.correct += 1
                        self.loop -= 1
                    elif userAnswer!=sol:
                        print("Incorrect, try again.\n")
                        self.incorrect += 1
        return (f"You got {self.correct} correct and {self.incorrect} incorrect\n")







    
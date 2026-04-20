# im deciding to create a class to handle
# lives, correctness, etc all in one place
import random

class mathGame():
    def __init__(self, operation, difficulty, lives, coins, incorrect, correct, loop):
        self.operation = operation
        self.difficulty = difficulty
        self.lives = lives
        self.coins = 0
        self.incorrect = 0
        self.correct = 0
        self.loop = 0

    def addition(self):
        if self.difficulty == 1:
            while True:
                self.loop = 5
                num1 = random.randint(0,9)
                num2 = random.randint(0,9)
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







    
# im deciding to create a class to handle
# lives, correctness, etc all in one place
import random

class mathGame():
    def __init__(self, operation, difficulty):
        self.operation = operation
        self.difficulty = difficulty
        self.coins = 0
        self.incorrect = 0
        self.correct = 0
        self.loop = 4
        self.lives = 3
        self.opSign = "+"

    def generateNum(self):
        if self.difficulty == "easy":
            num1 = random.randint(0,9)
            num2 = random.randint(0,9)
        elif self.difficulty == "medium":
            num1 = random.randint(10,99)
            num2 = random.randint(10,99)
        elif self.difficulty == "hard":
            num1 = random.randint(10,99)
            num2 = random.randint(99,999)
        numbers = num1, num2
        return numbers

    def problem(self):
        if self.operation == "add":
            while self.loop != 0:
                num1,num2 = self.generateNum()
                sol = num1+num2
                try:
                    userAnswer = int(input(f"{num1} + {num2} = "))
                except ValueError as e:
                    print("Error: enter a valid integer\n")
                else:
                    if userAnswer==sol:

                        self.correct += 1
                        self.coins += 10
                        self.loop -= 1
                        print(f"Correct! Your coins: {self.coins}\n")
                    elif userAnswer!=sol:
                        self.incorrect += 1
                        #self.lives -= 1
                        while userAnswer!= sol:
                            print("Incorrect, try again.\n")
                            try:
                                userAnswer = int(input(f"{num1} + {num2} = "))
                            except ValueError as e:
                                print("Error: enter a valid integer\n")
                            else:
                                if userAnswer == sol:
                                    print("Correct! But you don't get points for that.\n")
                                    
                            

        if self.operation == "sub":
            while self.loop != 0:
                num1,num2 = self.generateNum()
                sol = num1-num2
                try:
                    userAnswer = int(input(f"{num1} - {num2} = "))
                except ValueError as e:
                    print("Error: enter a valid integer\n")
                else:
                    if userAnswer==sol:
                        print("Correct!\n")
                        self.correct += 1
                        self.coins += 10
                        self.loop -= 1
                    elif userAnswer!=sol:
                        self.incorrect += 1
                        #self.lives -= 1
                        while userAnswer!= sol:
                            print("Incorrect, try again.\n")
                            try:
                                userAnswer = int(input(f"{num1} - {num2} = "))
                            except ValueError as e:
                                print("Error: enter a valid integer\n")
                            else:
                                if userAnswer == sol:
                                    print("Correct! But you don't get points for that.\n")
        if self.operation == "mul":
            while self.loop != 0:
                num1,num2 = self.generateNum()
                sol = num1*num2
                try:
                    userAnswer = int(input(f"{num1} * {num2} = "))
                except ValueError as e:
                    print("Error: enter a valid integer\n")
                else:
                    if userAnswer==sol:
                        print("Correct!\n")
                        self.correct += 1
                        self.coins += 10
                        self.loop -= 1
                    elif userAnswer!=sol:
                        self.incorrect += 1
                        #self.lives -= 1
                        while userAnswer!= sol:
                            print("Incorrect, try again.\n")
                            try:
                                userAnswer = int(input(f"{num1} * {num2} = "))
                            except ValueError as e:
                                print("Error: enter a valid integer\n")
                            else:
                                if userAnswer == sol:
                                    print("Correct! But you don't get points for that.\n")
                        
        print (f"You got {self.correct} correct and {self.incorrect} incorrect. You've earned a total of {self.coins} coins.\n")







    
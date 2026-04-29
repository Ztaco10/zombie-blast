# im deciding to create a class to handle
# lives, correctness, etc all in one place
import random
import json

class mathGame():
    def __init__(self, operation, difficulty):
        self.operation = operation
        self.difficulty = difficulty
        self.coins = 0
        self.incorrect = 0
        self.correct = 0
        self.loop = 8
        self.lives = 3
        self.opSign = "+"

    def setLives(self):
        if self.difficulty == "easy":
            self.lives = 5
        elif self.difficulty == "medium":
            self.lives = 3
        elif self.difficulty == "hard":
            self.lives = 2
        return self.lives

    def zombieAppears(self):
        return random.randint(1, 100) <= 30
    
    
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
    
    def setOpsign(self):
        if self.operation == "add":
            self.opSign = "+"
        elif self.operation == "sub":
            self.opSign = "-"
        elif self.operation == "mul":
            self.opSign = "*"
    

    def randomZombie(self):

        with open("zombie.json", "r") as f:
            zombies = json.load(f)

        return random.choice(zombies)
    
    def problemVerification(self):
        num1, num2 = self.generateNum()
        if self.operation == "add":
            sol = num1 + num2
        elif self.operation == "sub":
            sol = num1 - num2
        elif self.operation == "mul":
            sol = num1 * num2
        
        numbers = num1, num2, sol
        return numbers

    def problem(self):
        self.setLives()

        while self.loop != 0 and self.lives > 0:
            num1, num2, sol = self.problemVerification()
            zombieAppears = self.zombieAppears()

            if zombieAppears:
                zombie = self.randomZombie()
                print(f"🧟 {zombie['name']} appeared! Solve the problem to defeat it!\n")

            try:
                userAnswer = int(input(f"{num1} {self.opSign} {num2} = "))
            except ValueError:
                print("Error: enter a valid integer\n")
            else:
                if userAnswer == sol:
                    self.correct += 1
                    self.coins += 10
                    self.loop -= 1

                    if zombieAppears:
                        print(f"Correct! You defeated {zombie['name']}! Your coins: {self.coins}\n")
                    else:
                        print(f"Correct! Your coins: {self.coins}\n")

                else:
                    self.incorrect += 1

                    if zombieAppears:
                        self.lives -= 1
                        print(f"Wrong! {zombie['name']} attacked you! Lives left: {self.lives}\n")
                    else:
                        print("Incorrect, try again.\n")

        print(f"You got {self.correct} correct and {self.incorrect} incorrect. You've earned a total of {self.coins} coins.\n")

    def getCoins(self):
        return self.coins





    
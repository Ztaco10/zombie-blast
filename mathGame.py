# im deciding to create a class to handle
# lives, correctness, etc all in one place
from pathlib import Path
import random
import json
import database
from economy import Economy


class mathGame():
    def __init__(self, operation, difficulty, username=None):
        self.operation = operation
        self.difficulty = difficulty
        self.username = username

        if self.username:
            self.coins = database.getCoins(self.username, 0)
        else:
            self.coins = 0

        self.incorrect = 0
        self.correct = 0
        self.loop = 5
        self.lives = 3
        self.opSign = "+"

    def setLives(self):
        """
        Set the appropiate lives for each difficulty level
        """
        if self.difficulty == "easy":
            self.lives = 8

        elif self.difficulty == "medium":
            self.lives = 4

        elif self.difficulty == "hard":
            self.lives = 2


    def zombieAppears(self):
        """
        A chance that zombie appears during the gameplay
        """
        return random.randint(1, 100) <= 50
    
    
    def generateNum(self):
        """
        Generate two random numbers depending on the difficulty level
        """
        if self.difficulty == "easy":
            path = random.randint(1, 100) >= 50
            if path:
                num1 = random.randint(1,9)
                num2 = random.randint(1,9)
            else:
                num1 = random.randint(1, 9)
                num2 = random.randint(1, 99)

        elif self.difficulty == "medium":
            num1 = random.randint(10,99)
            num2 = random.randint(10,99)

        elif self.difficulty == "hard":
            path = random.randint(1,100) >= 70
            if path:
                num1 = random.randint(10,99)
                num2 = random.randint(100,999)
            else:
                num1 = random.randint(100,999)
                num2 = random.randint(100,999)
        numbers = num1, num2
        return numbers
    
    def setOpsign(self):
        """
        This is to make printing the problems easier to implement
        """
        if self.operation == "add":
            self.opSign = "+"
        elif self.operation == "sub":
            self.opSign = "-"
        elif self.operation == "mul":
            self.opSign = "*"
    

    def randomZombie(self):
        """
        Choose a random zombie
        """
        zombie_file = Path(__file__).parent / "zombie.json"
        with open(zombie_file, "r", encoding="utf-8") as f:
            zombies = json.load(f)

        return random.choice(zombies)
    
    def problemVerification(self):
        """
        Get the two numbers from generateNum and get the solution, return all the numbers
        """
        num1, num2 = self.generateNum()
        if self.operation == "add":
            sol = num1 + num2
        elif self.operation == "sub":
            sol = num1 - num2
        elif self.operation == "mul":
            sol = num1 * num2
        
        numbers = num1, num2, sol
        return numbers

    def saveCoins(self):
        """
        Save the current coin balance to the logged-in user's database record.
        """
        if self.username:
            database.updateCoins(self.username, self.coins)

    def problem(self):
        """
        Prints the problem and has a chance of zombie appearances, asks for user answer and verifies correctness.
        Lives are limited depending on difficulty
        """
        self.setLives()
        self.setOpsign()
        while self.loop != 0 and self.lives != 0:
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
                    self.saveCoins()
                    self.loop -= 1

                    if zombieAppears:
                        print(f"Correct! You defeated {zombie['name']}! Your coins: {self.coins}\n")
                    else:
                        print(f"Correct! Your coins: {self.coins}\n")

                else:
                    self.incorrect += 1
                    self.loop -=1

                    if zombieAppears:
                        self.lives -= 1
                        print(f"Wrong! {zombie['name']} attacked you! Lives left: {self.lives}\n")
                    else:
                        print("Incorrect, try again.\n")

        print(f"You got {self.correct} correct and {self.incorrect} incorrect. You've earned a total of {self.coins} coins.\n")

    def getCoins(self):
        return self.economy.get_balance()





    

# im deciding to create a class to handle
# lives, correctness, etc all in one place

class mathGame():
    def __init__(self, operation, difficulty, lives, coins, incorrect, correct):
        self.operation = operation
        self.difficulty = difficulty
        self.lives = lives
        self.coins = 0
        self.incorrect = incorrect
        self.correct = correct
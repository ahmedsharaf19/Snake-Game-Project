from turtle import Turtle

class Score(Turtle):
    
    def __init__(self, player_name):
        super().__init__()
        self.score = 0
        self.ht()
        self.penup()
        self.goto(0, 270)
        self.color('white')
        self.write(arg =f'{player_name} Score : {self.score}', align='center', font=['Arial', 15, 'normal'])

        
    def game_over(self):
        self.goto(0,0)
        self.write(arg =f'GAME OVER.', align='center', font=['Arial', 15, 'normal'])
    def increase_score(self, player_name):
        self.score += 1
        self.clear()
        self.write(arg =f'{player_name} Score : {self.score}', align='center', font=['Arial', 15, 'normal'])
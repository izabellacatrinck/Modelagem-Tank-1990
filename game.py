from tank import Tank
from ball import Ball
from maze import Maze

class Game:

    def __init__(self, x, y):
        self.tank = Tank(x = 40, y = 50)
        self.ball = Ball()
        self.maze = Maze()

    def running(self):
        print("Game is running")

    def start_game(self):
        print("Game started")
        self.tank.move()
        self.tank.shoot()
        self.ball.move()
        self.maze.walls()
        self.maze.spawn_map()
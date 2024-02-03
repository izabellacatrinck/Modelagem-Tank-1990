class Tank:


    def __init__(self, x, y):
        self.x = x
        self.y = y

    def shoot(self):
        print("Tank is shooting")

    def move(self):
        print("Tank is moving")

    def printing(self,x , y):
        print(f"\nTank recebe: {x}, {y}\n")
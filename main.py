from game import Game


def main():
    x= 40
    y = 50
    game = Game(x, y)
    game.start_game()
    game.running()

if __name__ == "__main__":
    main()
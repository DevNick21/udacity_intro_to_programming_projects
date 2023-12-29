"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        choice = input("Rock, Paper, Scissors? ").lower()
        while choice not in moves:
            choice = input("Rock, Paper, Scissors? ").lower()
        return choice


class ReflectPlayer(Player):
    def __init__(self):
        self.their_move = None

    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):
    def __init__(self):
        self.my_move = None

    def learn(self, my_move, their_move):
        move_index = moves.index(my_move)
        if move_index == 2:
            move_index = -1
        self.my_move = moves[move_index + 1]

    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            return self.my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0
        self.isGameOver = False

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player One: {move1}  Player Two: {move2}")
        if move1 == "quit" or move2 == "quit":
            self.isGameOver = True
        elif move1 == move2:
            print("TIE")
        else:
            if beats(move1, move2):
                self.p1_score += 1
                print("PLAYER ONE WINS")

            elif beats(move2, move1):
                self.p2_score += 1
                print("PLAYER TWO WINS")
        print(
            f"""Score:
            Player One: {self.p1_score}
            Player Two: {self.p2_score}""")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        while self.isGameOver is False:
            print("Game start!")
            for round in range(8):
                print(f"Round {round}:")
                self.play_round()
            self.isGameOver = True
        print("Game over!")
        if self.p1_score == self.p2_score:
            print(f"""
            ITS A TIE!
            Player One: {self.p1_score}
            Player Two: {self.p2_score}""")
        elif self.p1_score > self.p2_score:
            print(f"""
            PLAYER ONE wins!
            Player One: {self.p1_score}
            Player Two: {self.p2_score}""")
        elif self.p1_score < self.p2_score:
            print(f"""
            PLAYER TWO wins!
            Player One: {self.p1_score}
            Player Two: {self.p2_score}""")


if __name__ == '__main__':
    opponents = [
        Player(),
        RandomPlayer(),
        ReflectPlayer(),
        CyclePlayer()
    ]
    p1 = HumanPlayer()
    p2 = random.choice(opponents)
    game = Game(p1, p2)
    game.play_game()

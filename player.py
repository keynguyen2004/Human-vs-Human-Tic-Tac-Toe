import math
import random
import re

class FirstPlayer:
    def GetFirstPlayer(self):
        flag = False
        # Choose the first player
        while flag == False:
            firstPlayer = input("Choose the first player (X/O): ")
            try:
                if not (firstPlayer == "X" or firstPlayer == "O"):
                    raise TypeError
                else:
                    flag = True
            except TypeError:
                print("Incorrect. Please enter either 'X' or 'O' as the first player: ")    
        
        return firstPlayer

class Player:
    def __init__ (self, letter):
        # letter is either X or O
        self.letter = letter

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)  # Call the initialization of the superclass Player
    
    # we want all players to get their next move given a game
    def getMove(self, game, letter):
        flag = False
        while flag == False:
            square = input(letter + "'s turn. Input move (1 to 9): ")
            try:
                if not square.isnumeric():
                    raise TypeError
                elif int(square) - 1 not in game.availableMoves():
                    raise ValueError
                else:
                    square = int(square)
                    flag = True
            except TypeError:
                print("Wrong data type. Please input move (1 to 9): ")
            except ValueError:
                print("Spot already taken. Please input another move : ")
        
        return square
               
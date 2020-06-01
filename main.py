import sys
import random
class Hangman:
    def __init__(self):
        self.board = []
        self.lives = 6
        self.words = ['papaya','bannana','berry','pinapple','mango','cherry','strawberry','blueberry','avocado','passionfruit']
        self.winword = ''
    def main(self):
        start = input('Start new game? Y/N ').lower()
        if start == 'y':
            self.winword = random.choice(self.words).lower()
            self.set_up()
            self.play()
        else:
            sys.exit('ttyl :)')
    def set_up(self):
        for ch in range(len(self.winword)):
            self.board.append('_')
    def play(self):    
        guessed = []
        while self.lives > 0:           
            letter = input('Guess a letter :')           
            if letter in self.winword and letter not in guessed:
                guessed.append(letter)
                self.refreshBoard(letter)
                self.checkIfWin()
            elif letter in guessed:
                print("You have already guessed this letter! Try again!")
            else:
                guessed.append(letter)
                print("That letter does not exist in the word! Try again")
                self.lives -= 1
            print(self.board)
        print('You are out of lives! The word was ' + self.winword)

    def refreshBoard(self,letter):
        for i, ch in enumerate(self.winword):
            if letter == ch:
                self.board[i] = letter
    def checkIfWin(self):
        board_str = ''.join([str(ch) for ch in self.board])
        if board_str == self.winword:
            print("Congrats! you won :)")
            sys.exit()

new_game = Hangman()
new_game.main()

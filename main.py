import random
import sys
class Hangman:
    def __init__(self):
        self.board = []
        self.lives = 6
        self.words = ['papaya','bannana','berry','pinapple','mango','cherry','strawberry','blueberry','avocado','passionfruit']
        self.winword = ''
    def main(self):
        start = input('Start new game? Y/N :').lower()
        print(start)
        if start == 'y':                      
            self.winword = self.pick_word(self.words)
            self.set_up()
            self.play()
        else:
            sys.exit('ttyl :)')
    def pick_word(self,words):
        word = random.choice(words)
        return word.lower()
    def set_up(self):
        for ch in range(len(self.winword)):
            self.board.append('_') 
    def play(self):
        print(self.board)
        guessed = []
        while self.lives > 0:
            letter = input('Guess a letter :')    
            if letter in self.winword and letter not in guessed:
                self.refreshBoard(letter)
                self.checkIfWin()
                guessed.append(letter)     
            elif letter in guessed:
                print("You have already guessed this letter! Try again") 
                print(self.board)
            else:
                guessed.append(letter)
                print("That letter does not exist in the word! Try again")
                print(self.board)
                self.lives -= 1
        print('You are out of lives! The word was '+ self.winword)
    def refreshBoard(self,letter):
        for i, ch in enumerate(self.winword):
            print("Great! It's a match!")
            if letter == ch: 
                self.board[i] = letter
        print(self.board)
    def checkIfWin(self):
        board_str = ''.join([str(ch) for ch in self.board]) 
        if board_str == self.winword:
            print("Congrats! You won! :)")
            sys.exit()

new_game = Hangman()
new_game.main()


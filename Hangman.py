import random

"""This program recreates the classic Hangman game. Player One picks a secret
   word and draws a line for each letter in it. Player Two tries to guess the
   word one letter at a time. If Player Two guesses a letter correctly, Player One
   replaces the corresponding underscore with the correct letter. In this version
   of the game, if a letter appears twice in a word, you have to guess it twice.
   OR
   If Player Two guesses incorrectly, Player One draws a body part of a hanged stick
   figure (starting with the heaad). If Player Two completes the word before the drawing
   of the hangmen is complete, they win. If not, they lose."""

def hangman():
    words = ["Loyalty", "Bank", "Church", "Spirit", "Football", "Diamond",
             "Future", "Source", "City", "Pen", "Apple", "Zoo", "Welcome",
             "Asylum", "Forest", "Mind", "Quiz", "Squirrel", "Vanity", "Run",
             "Exercise", "Journal", "Young", "Rush", "Various", "House", "Garnet",
             "Island", "Karma", "Laundry", "Mountain", "Nature", "Orion", "Purify",
             "Tremendous", "Unique"]
    word = random.choice(words)
    wrong = 0
    #Keeps track of how many incorrect letters were guessed
    stages = ["",
              "___________            ",
              "|                      ",
              "|           |          ",
              "|           0          ",
              "|          /|\         ",
              "|          / \         ",
              "|                      ",
              ]
    rletters = list(word)
    #List containing each character in the word
    board = ["__"] * len(word)
    #List of strings used to keep track of the hints that's displayed
    win = False
    print("Welcome to Hangman")

    #Continues as long as the player doesn't guess more wrong letters than the strings that makes up the hangman
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter "
        char = input(msg)
        #Collects guesses from user

        #If guessed correctly, get the index of that letter and replace underscore with letter
        #Replace letter in rletters with a dollar sign to mark it guessed
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        
        #Start from stage 0, and slice up to current stage
        #This slice gives only the strings needed to print the current hangmen
        e = wrong + 1
        print("\n".join(stages[0: e]))
        #If there are no more underscores on the board, the game is won 
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))

hangman()
            

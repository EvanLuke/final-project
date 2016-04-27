


import random
words = ["cat", "dog", "monkey", "mule", "giraffe", "zebra", "snake", "elephant"]

print('Welcome to hangman! A random word will be chosen, guess the word one letter at a time. Enter a single lowercase letter. Once you guess 10 wrong letters the game will end and show you the word. As you guess the right letters it will fill in the dashes.')

def getRandomword(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList [wordIndex]

def getGuess():
    while True:
        print('Guess a letter')
        print('You have ' +str(mistakes)+ ' mistakes left') 
        
        guess = input()
        guess = guess.lower()
        if guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER!')
        elif guess in alreadyGuessed:
            print('You already chose that, choose another letter.')
        elif len(guess) != 1:
            print('Please enter a single lowercase letter')
        else:
            return guess


secretWord = getRandomword(words)
alreadyGuessed= set()
board = "-" * len(secretWord)
mistakes = 10


while True:
    guess = getGuess()
    print(board)
    if mistakes < 1:
        print('Sorry, too many mistakes, the word is ' + secretWord + '!')
        break
    
    elif guess in secretWord:
        alreadyGuessed.add(guess)
        board = "".join([char if char in alreadyGuessed else "-" for char in secretWord])
        print('Correct ' + str(guess) + ' is in the word')
        
        if board == secretWord:
            print('You won ' +str(secretWord) + ' is the word!')
            break
            
        continue
    elif guess not in secretWord:
        mistakes -= 1
        print('Wrong ' + str(guess) + ' is not in the word')
        
        continue


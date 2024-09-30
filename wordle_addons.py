from random import random

def list_convert(word):
    # Converts the word into a list
    convert = []
    i = 0 
    while i < len(word):
        convert+=word[i]
        i+=1
    
    return convert

def str_convert(word):
    # Converts the word into a string 
    convert = ''
    i = 0
    while i < len(word):
        convert+=word[i]
        i+=1 
    return convert
    
def case_insentivity(guesswordlist):
    alphabetupper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    alphabetlower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in range(0,26):
        for j in range (0,5):
            if alphabetlower[i] == guesswordlist[j]:
                for k in range(0,26):
                    if i == k:
                        guesswordlist[j] = alphabetupper[k]

    return guesswordlist

def change_guess(changeGuesses):
    if changeGuesses == 'y' or changeGuesses == 'Y':
        guessesinput = int(input('Number of guesses: '))
    elif changeGuesses == 'n' or changeGuesses == 'N': 
        guessesinput = 6
    
    return guessesinput

def random_word():
    words = 'ABACK','ABASE','BALMY','BASIS','BASTE','BATCH', 'CAROL','CHAIR', 'DELVE','DENSE','EDICT','ERASE','FINER','FLAIR','GLAZE','GOOSE','HABIT','HELLO','IMPLY','INDEX','KNOCK','KEBAB','LARGE','LARVA','MAJOR','MOCHA','OCEAN','ORBIT'
    wordpick = int(random() * 26)
 
    random_wordpick = words[wordpick]
    
    return random_wordpick

def alphabet_checker(word, alphabetglobal):
    alphabetlocal = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(0,len(alphabetglobal)):
            for j in range (0,5):
                if alphabetglobal[i] == word[j]:
                    alphabetglobal[i] = ''

    new = []
    for i in range(0, 26):
        for j in range(0,len(alphabetglobal)):
            if alphabetglobal[i] == alphabetlocal[j]:
                new+=str(alphabetlocal[j] + ' ')

    return new
    
def check_len_word():
    while True:
        wordstring = input()
        if len(wordstring) == 5:
            return wordstring
        else:
            print('Please enter a valid input: \n')

def check_len_initial(word):
    if len(word) == 5:
        return word
    else:
        print('Please input a valid (5) letter word')
        initialWord = str(input('Please enter a valid: \n'))
        start_wordle(initialWord)

def start_wordle():
        
        initialWord = str(input('Please enter a word for the player to guess: \n'))

        if initialWord == 'RANDOM':
            initialWord = random_word()
        elif initialWord == 'QUIT':
            return 0 
        else:
            initialWord = check_len_initial(initialWord)

        #Turn lower case letter to uppercase
        guessinitialWord = list_convert(initialWord)
        initialWord = str_convert(case_insentivity(guessinitialWord))

        #call the function to change the guess
        changeGuesses = str(input('Do you want to change the number of guesses (y/n): \n'))

        guesses = change_guess(changeGuesses)

        alphabetglobal = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        #start of the game
        print(f'Guess the word, {guesses} guess(es) left: -----')
        while True:
            while guesses != 0:

                guesses-=1

                guesswordstring = check_len_word()
                guesswordlist = list_convert(guesswordstring)
                word = str_convert(case_insentivity(guesswordlist))

                print(str_convert(alphabet_checker(word, alphabetglobal)))

                result = compare_wordle(initialWord, word)

                # Check the return values is True or False and return the final list 
                if result[0]:
                    print('Congratulations! You win!')
                    exit()
                else:
                    if guesses != 0:
                        print(f'Guess the word, {guesses} guess(es) left: {result[1]} \n')

            if guesses == 0:
                print('SORRY, YOU LOSE!')



def compare_wordle(initialWord, word):
    # If the user gets the correct word
    if word == initialWord:
        return (1, initialWord)
    
    # If both words are not the same
    s = ['?', '?', '?', '?', '?']
    for i in range(0,5):
        if word[i] == initialWord[i]:
            s[i] = word[i]
        else:
            for j in range(0,5):
                # To implement the new rule remove the same letter once ONE position or the same amount 
                # of number (letters) has been found
                if initialWord[j] == word[i]:
                    s[i] = '!'
                    break
    return (0, s)

start_wordle()
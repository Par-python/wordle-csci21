# John Jerome C. Pardo
# 246268
# October 1, 2024

# I have not discussed the Python language code in my program 
# with anyone other than my instructor or the teaching assistants 
# assigned to this course.

# I have not used Python language code obtained from another student, 
# or any other unauthorized source, either modified or unmodified.

# If any Python language code or documentation used in my program 
# was obtained from another source, such as a textbook or website, 
# that has been clearly noted with a proper citation in the comments 
# of my program.

import random

initialWord = str(input('Please enter a word for the player to guess: \n'))

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
    guesswordlist = list_convert(guesswordlist)

    alphabetupper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    alphabetlower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in range(0,26):
        for j in range (0,len(guesswordlist)):
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
    wordpick = int(random.random() * 26)
 
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
        return check_alphabet_initial(word)
    else:
        print('Please input a valid (5) letter word')
        initialWord = str(input('Please enter a valid input: \n'))
        start_wordle(initialWord)

def check_alphabet_initial(word):
    nonumbercount = 0
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    for i in range (0,42):
        for j in range(0,5):
            if alphabet[i] == word[j]:
                nonumbercount+=1

    if nonumbercount == 5:
        return word
    else: 
        initialWord = str(input('Please enter a word for the player to guess: \n'))
        start_wordle(initialWord)

def start_wordle(initialWord):
        
        initialWord = str_convert(case_insentivity(initialWord))
        
        if initialWord == 'RANDOM':
            initialWord = random_word()
        elif initialWord == 'QUIT':
            return 0 
        else:
            initialWord = check_len_initial(initialWord)

        #call the function to change the guess
        changeGuesses = str(input('Do you want to change the number of guesses (y/n): \n'))

        guesses = change_guess(changeGuesses)

        alphabetglobal = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        
        initialalphabet = []
        i = 0
        while i < len(alphabetglobal):
            initialalphabet+= str(alphabetglobal[i] + ' ')
            i+=1
        
        print(str_convert(initialalphabet))

        #start of the game
        print(f'Guess the word, {guesses} guess(es) left: -----')
        while True:
            while guesses != 0:

                check = False

                guesses-=1

                guesswordstring = check_len_word()
                guesswordlist = list_convert(guesswordstring)
                word = str_convert(case_insentivity(guesswordlist))
                
                
                
                print(str_convert(alphabet_checker(word, alphabetglobal)))

                result = compare_wordle(initialWord, word)

                # Check the return values is True or False and return the final list 
                if result[0]:
                    print('Congratulations! You win!')
                    initialWord = str(input('Please enter a word for the player to guess: \n'))
                    if str_convert(case_insentivity(initialWord)) == 'QUIT':
                        check = True 
                        break
                    start_wordle(initialWord)
                else:
                    if guesses != 0:
                        print(f'Guess the word, {guesses} guess(es) left: {result[1]} \n')

            if check == True:
                break

            if guesses == 0:
                print('SORRY, YOU LOSE!')
                initialWord = str(input('Please enter a word for the player to guess: \n'))
                if str_convert(case_insentivity(initialWord)) == 'QUIT':
                    check = True
                    break
            if check == True:
                break
            start_wordle(initialWord)

def compare_wordle(initialWord, word):
    # If the user gets the correct word
    if word == initialWord:
        return (1, initialWord)
    
    # If both words are not the same
    initialWord = list_convert(initialWord)
    oldinitialWord = initialWord
    # both words are not the same
    s = ['?', '?', '?', '?', '?']
    for i in range(0,5):
        if word[i] == initialWord[i]:
            s[i] = word[i]
            initialWord[i] = ' '
            
    for i in range(0,5):
        if word[i] == s[i]:
            continue
        for j in range(0,5):
            if word[i] == initialWord[j]:
                s[i] = '!'
                initialWord[j] = ' '
                break
    
    return (0, s)

start_wordle(initialWord)
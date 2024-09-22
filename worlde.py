initialWord = str(input('Please enter a word for the player to guess: \n'))
changeGuesses = str(input('Do you want to change the number of guesses (y/n): \n'))

def startwordle(initialWord, changeGuesses):
    # Initiliaze the default settings
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Check if the input is equal to five and convert the initial word + word to a list 
    if len(initialWord) == 5:
        initialWordConvert = []
        i = 0  
        while i < len(initialWord):
            initialWordConvert.append(initialWord[i])
            i+=1  
    else:
        print('Not a vaild (5 letter) initial word')
        return 0 
    
    if changeGuesses == 'y':
        guesses = int(input('Number of guessses: '))
    elif changeGuesses == 'n':
        guesses = 6 
    else:
        print('Select a valid input')
    
    #Check guesses
    print('Guess the word, ' + str(guesses) + ' guess(es) left: -----')
    while guesses != 0:

        guesses-=1

        word = input()

        if len(word) == 5:
            wordConvert = []
            i = 0  
            while i < len(word):
                wordConvert.append(word[i])
                i+=1  
        else:
            return 0, print('Not a vaild (5 letter) guess word')

        result = comparewordle(wordConvert, initialWordConvert, initialWord, word)

        # Check the return values is True or False and return the final list 
        if result[0]:
            print('Congratulations! You win!')
            exit()
        else:
            if guesses != 0:
                print('Guess the word, ' + str(guesses) + ' guess(es) left:' + str(result[1]) + '\n')

 
    print('SORRY, YOU LOSE!')

def comparewordle(wordConvert, initialWordConvert, initialWord, word):

    # If the user gets the correct word
    if word == initialWord:
        return (1, initialWord)
    
    # If both words are not the same
    s = ['?', '?', '?', '?', '?']
    for i in range(0,5):
        # Change if in 
        if wordConvert[i] == initialWord[i]:
            s[i] = wordConvert[i]
        else:
            for j in range(0,5):
                if initialWord[j] == wordConvert[i]:
                    s[i] = '!'
                    break
    return (0, s)

startwordle(initialWord, changeGuesses)

# Incorrect position is!
# Wrong letter is ?
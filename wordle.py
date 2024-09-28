initialWord = str(input('Please enter a word for the player to guess: \n'))

def startWordle(initialWord):

    guesses = 6

    while guesses != 0:

        print(f'Guess the word, {guesses} guess(es) left: -----')

        guesses-=1

        word = input()

        result = compareWordle(initialWord, word)

        # Check the return values is True or False and return the final list 
        if result[0]:
            print('Congratulations! You win!')
            exit()
        else:
            if guesses != 0:
                print(f'Guess the word, {guesses} guess(es) left: {result[1]} \n')

    print('SORRY, YOU LOSE!')

def compareWordle(initialWord, word):

    # If the user gets the correct word
    if word == initialWord:
        return (1, initialWord)
    
    # If both words are not the same
    s = ['?', '?', '?', '?', '?']
    for i in range(0,5):
        if list(word)[i] == initialWord[i]:
            s[i] = word[i]
        else:
            for j in range(0,5):
                if initialWord[j] == list(word)[i]:
                    s[i] = '!'
                    break
    return (0, s)

startWordle(initialWord)
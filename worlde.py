word = input()

def startwordle(word):
    # Initiliaze the default settings
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    guesses = 6
    initialWord = 'WORDS'

    # Check if the input is equal to five and convert the initial word + word to a list 
    if len(word) == 5:
        wordConvert = []
        initialWordConvert = []
        i = 0  
        while i < len(word):
            wordConvert.append(word[i])
            initialWordConvert.append(initialWord[i])
            i+=1  

        compareworlde(wordConvert,initialWordConvert)
    else: 
        return 0

def compareworlde(wordConvert, initialWordConvert):
    s= []

    for x in initialWordConvert:
        if x in wordConvert:
            i = 0 
                  

startwordle(word)

# Incorrect position is !
# Wrong letter is ?


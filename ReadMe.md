# WORDLE PROJECT

This ReadMe will show the base game and the add ons as seperate games. To show how it was built AROUND
the first 'iteration' of the game

## Base Game
In this project we are tasked to make a wordle game. For the base game there are only functions needed:

```py
    def start_wordle(initialWord):
        
        guesses = 6
        while guesses != 0:

            guesses-=1

            word = input()
            result = compare_wordle(initialWord, word)

            # Check the return values is True or False and return the final list 
            if result[0]:
                print('Congratulations! You win!')
                break
            else:
                if guesses != 0:
                    print(f'Guess the word, {guesses} guess(es) left: {result[1]} \n')
        if guesses == 0:
            print('SORRY, YOU LOSE!')
```
- This function is used to start the game and take the initialWord(the word to be guessed) and gives to the other function
called compare_wordle(), which looks like this:

```py
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
```

## Add ons

## Check Word Length

- For the first add on 'Check Word length'. After the user inputs the word to be guessed the function called is tasked check if the
word has exactly 5 valid letters.

```py
def check_len_initial(word):
    if len(word) == 5:
        return check_alphabet_initial(word)
    else:
        print('Please input a valid (5) letter word')
        initialWord = str(input('Please enter a valid input: \n'))
        start_wordle(initialWord)
```

This returns the value of the word and goes to the next function to check if the inputs are in the alphabet and if it is not exactly
five words it will ask again the user for a prompt and initial the game again for it to take in the new input.

```py
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
```
After it checks that the input has 5 letters/characters it will move on to check_alphabet_initial(word) where the input is checked if it is in the alphabet using the variable alphabet as a string to loop through the inputs and check if each one correspands to a character in it. If it does it adds it to the numbercount and if not it will skip. The value only gets returned if exactly 5 are on the list.

##  Case Insensitivity 

```py
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
```

In this function it will get the guesswordlist or the word that was guessed by the user and turned into a list get the lower case values and then replace it with the uppercase value. This will return a value where every letter is uppercase.

## Change number of guesses
```py 
    changeGuesses = str(input('Do you want to change the number of guesses (y/n): \n'))

    guesses = change_guess(changeGuesses)
```
The user is asked if they want to change the number of their guesses and it passes it the guesses where it calls the function 
change_guess(changeGuesses) to check their response

```py
    def change_guess(changeGuesses):
    if changeGuesses == 'y' or changeGuesses == 'Y':
        guessesinput = int(input('Number of guesses: '))
    elif changeGuesses == 'n' or changeGuesses == 'N': 
        guessesinput = 6
    
    return guessesinput
```
If the user inputs Y or y the function will ask the player what number would they prefer for the game and return it. While if the user inputs N or n the function will just return the default number of guesses based on the specifications which is 6 guesses.
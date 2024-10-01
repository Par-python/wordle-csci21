# initialWord = 'HELLO'
# word = input()

# initialWord = list(initialWord)
# oldinitialWord = initialWord
# # both words are not the same
# s = ['?', '?', '?', '?', '?']
# for i in range(0,5):
#     if word[i] == initialWord[i]:
#         s[i] = word[i]
#         initialWord[i] = ' '

# print(initialWord)
        
# for i in range(0,5):
#     if word[i] == s[i]:
#         continue
#     for j in range(0,5):
#         if word[i] == initialWord[j]:
#             s[i] = '!'
#             initialWord[j] = ' '
#             break

# print(s)

# word = 'HELL5'

# nonumbercount = 0
# alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# for i in range (0,26):
#     for j in range(0,5):
#         if alphabet[i] == word[j]:
#             nonumbercount+=1

# if nonumbercount == 5:
#     print('Valid Input')
# else: 
#     print('Input/s are not valid')

alphabetglobal = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

word = input()

guesses = 6

initialguesses = 5

def alphabet_checker(word, alphabetglobal, guesses, initialguesses):
    if guesses == initialguesses:
         print('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z')
         word = input()
         return word
    else:
        word = input()
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

if word == 'ALPHABET':
    print(alphabet_checker(word, alphabetglobal, guesses, initialguesses))
else:
     print('bruh')

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

def alphabet_checker(word, alphabetglobal):
    alphabetlocal = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    print(f'{alphabetglobal} let')

    for i in range(0,len(alphabetglobal)):
            for j in range (0,5):
                if alphabetglobal[i] == word[j]:
                    alphabetglobal[i] = ''

    new = []
    for i in range(0, 26):
        for j in range(0,len(alphabetglobal)):
            if alphabetglobal[i] == alphabetlocal[j]:
                new+=str(alphabetlocal[j] + ' ')

    alphabetlet = new

    return new


# new = []
# for i in (0, len(str_convert(alphabetlet))):
#     for j in (0, len(str_convert(alphabetconst))):
#         if alphabetlet[i] == alphabetconst[j]:
#             new+=str(alphabetlet[j])

alphabetglobal = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

i = 0
while i <= 6:
    word = input()
    word = list_convert(word)

    alphabetlet = alphabet_checker(word, alphabetglobal)
    print(str_convert(alphabet_checker(word, alphabetglobal)))
    i+=1
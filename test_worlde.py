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

def alphabet_checker(word):
    alphabetlet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    alphabetconst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for i in range(0,26):
            for j in range (0,5):
                if alphabetlet[i] == word[j]:
                    alphabetlet[i] = ''

    new = []
    for i in range(0, len(str_convert(alphabetconst))):
        for j in range(0,len(str_convert(alphabetlet))):
            if alphabetconst[i] == alphabetlet[j]:
                new+=str(alphabetlet[j] + ' ')
    
    alphabetlet = new

    return str_convert(new)


# new = []
# for i in (0, len(str_convert(alphabetlet))):
#     for j in (0, len(str_convert(alphabetconst))):
#         if alphabetlet[i] == alphabetconst[j]:
#             new+=str(alphabetlet[j])

alphabetlet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

i = 0
while i <= 6:
    word = input()
    word = list_convert(word)

    print(str_convert(alphabet_checker(word)))
    alphabetlet = alphabet_checker(word)
    print(i)
    i+=1
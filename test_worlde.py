initialWord = str(input('Please enter a word for the player to guess: \n'))
word = str(input('Enter a word to guess: '))

i = 0
wordConvert = []
initialWordConvert = []
while i < len(word) and i < len(initialWord):
    wordConvert.append(word[i])
    initialWordConvert.append(initialWord[i])
    i+=1

if word == initialWord:
    print('Congratulations! You won!')
    exit()

s = ['?', '?', '?', '?', '?']
for i in range(0,5):
    # Change if in 
    if wordConvert[i] == initialWord[i]:
        s[i] = wordConvert[i]
    else:
        match = False

        for j in range(0,5):
            if initialWord[j] == wordConvert[i]:
                match = True
                break

        if match == True:
            s[i] = '!'
            
print(s)

# # Incorrect position is!
# # Wrong letter is ?

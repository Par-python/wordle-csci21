initialWord = 'HELLO'
word = input()

initialWord = list(initialWord)
oldinitialWord = initialWord
# both words are not the same
s = ['?', '?', '?', '?', '?']
for i in range(0,5):
    if word[i] == initialWord[i]:
        s[i] = word[i]
        initialWord[i] = ' '

print(initialWord)
        
for i in range(0,5):
    if word[i] == s[i]:
        continue
    for j in range(0,5):
        if word[i] == initialWord[j]:
            s[i] = '!'
            initialWord[j] = ' '
            break

print(s)
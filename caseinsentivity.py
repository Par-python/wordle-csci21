l = list(input())
word = list('HELLO')

def check_if_alphabet(word):
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    print(word)
    s = False
    while True:
        for j in range(0,26):
            if alphabet[j] == word:
                s = True
                break
        return s
    
s = ['?','?','?','?','?']
for i in range(0,5):
    for j in range(0,5):
        if word[i] == l[j] and check_if_alphabet(word[i]):
            s[i]='!'
    word[i] = ' '

print(s)


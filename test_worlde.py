from random import random

def random_word():
    words = 'ABACK','ABASE','BALMY','BASIS','BASTE','BATCH', 'CAROL','CHAIR', 'DELVE','DENSE','EDICT','ERASE','FINER','FLAIR','GLAZE','GOOSE','HABIT','HELLO','IMPLY','INDEX','KNOCK','KEBAB','LARGE','LARVA','MAJOR','MOCHA','OCEAN','ORBIT'
    wordpick = int(random() * 26)
 
    random_wordpick = words[wordpick]
    
    return random_wordpick

print(random_word())




# def word_pick(words,wordpick):
#     s = ''
#     if wordpick < 26:
#         s+=words[wordpick]
#     else:   
#         print('out of index')

#     return s

# random_word()
initalword = 'hello'

def list_convert(word):
    convert = []
    i = 0 
    while i < len(word):
        convert+=word[i]
        i+=1
    
    return convert

word = list_convert(initalword)

def f(word):
    alphabetupper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    alphabetlower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    s = []
    for i in range(0,26):
        for j in range (0,5):
            if alphabetlower[i] == word[j]:
                s+=word[j]
                for k in range(0,26):
                    if i == k:
                        word[j] = alphabetupper[k]

    return word
    
print(f(word))
import itertools

valid_words = []
words = []
l = []
dic = {}
score = 0
scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,   
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}                       #dict of the scores assigned to each English alphabet


rack = raw_input('Enter rack of words: ')       #taking rack of word from the user
fp = open('sowpods.txt', 'r')                   #reading SOWPODS file

for line in fp.readlines():
    word = line.strip()
    words.append(word)                          #making list of all the words in the file

for i in range(1, len(rack)+1):
    l = list(itertools.permutations(rack, i))   #finding permutations of the rack of all possible lengths
    for key in l:
        string = ''.join(map(str, key))
        #print string
        if string.upper() in words:             #checking whether word is present in the file
            valid_words.append(string)          #if YES, it's a valid word and so appended to the list 

fp.close()
for word in set(valid_words):
    for letter in word.lower():
        score += scores[letter]                 #calculating scores per word
    dic.update({word : score})                  #adding valid words with their scores to the dict 
    score = 0
    
print 'All the valid words are....'
for key in sorted(dic):
    print dic[key], key                         #printing score and valid word pair from the dict

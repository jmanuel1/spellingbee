# Open list of correcly-spelled words.
wordFile = open("words.txt")
threshold = 8
listOfWords = input().split()
index = 0

def lev(a, b):
    if min(len(a), len(b)) == 0:
        return max(len(a), len(b))
    else:
        return min(lev(a[:-1], b) + 1, lev(a, b[:-1]) + 1, 
            lev(a[:-1], b[:-1]) + int(not a == b))

for x in listOfWords:
    replacement = (x, threshold + 1)
    
    for word in wordFile:
        x = x.lower()
        word = word[:-1].lower()
        
        if x == word: 
            replacement = (x, 0)
            break # Some words may actually be spelled correctly!
        
        d = lev(x, word)
        if (d < threshold) and (replacement[1] > d):
            replacement = (word, d)
            
    listOfWords[index] = replacement[0]
    index += 1
    
print(*listOfWords)

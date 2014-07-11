# Open list of correcly-spelled words.
wordFile = open("words.txt")
threshold = 8
listOfWords = input().split()
index = 0

# Compute Levenshtein distance


def lev(a, b):
    if min(len(a), len(b)) == 0:
        return max(len(a), len(b))
    elif len(a) == len(b):
        # Use Hamming Distance (special case)
        return sum(x != y for x, y in zip(a, b))
    else:
        return min(lev(a[:-1], b) + 1, lev(a, b[:-1]) + 1,
                   lev(a[:-1], b[:-1]) + int(not a[-1] == b[-1]))

for x in listOfWords:
    replacement = (x, threshold + 1)

    for word in wordFile:
        x = x.lower()
        word = word[:-1].lower()

        if x == word:
            replacement = (x, 0)
            break  # Some words may actually be spelled correctly!

        d = lev(x, word)
        if (d < threshold) and (replacement[1] > d):
            replacement = (word, d)

    listOfWords[index] = replacement[0]
    index += 1
    wordFile.seek(0)

print(*listOfWords)

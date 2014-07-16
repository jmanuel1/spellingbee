# Open list of correcly-spelled words.
wordFile = open("words.txt")
THRESHOLD = 1
listOfWords = input().split()
index = 0

# Compute Levenshtein distance


def lev(a, b):
    d = [[0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]

    for i in range(1, len(a) + 1):
        d[i][0] = i

    for j in range(1, len(b) + 1):
        d[0][j] = j

    for j in range(1, len(b) + 1):
        for i in range(1, len(a) + 1):
            if a[i - 1] == b[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = min(
                    d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + 1)

    return d[len(a)][len(b)]

# Length of longest common subsequence


def lcsLen(a, b):
    C = [[0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
            else:
                C[i][j] = max(C[i][j - 1], C[i - 1][j])

    return C[len(a)][len(b)]

# String match score


def matchScore(a, b):
    return (lev(a, b) - lcsLen(a, b)) / 2

for x in listOfWords:
    replacement = (x, THRESHOLD + 1)

    for word in wordFile:
        x = x.lower()
        word = word[:-1].lower()

        if x == word:
            replacement = (x, 0)
            # Some words may actually be spelled correctly!
            break

        d = matchScore(x, word)
        if (d < THRESHOLD) and (replacement[1] > d):
            replacement = (word, d)

    listOfWords[index] = replacement[0]
    index += 1
    wordFile.seek(0)

print(*listOfWords)

"""spellingbee.py -- Module to help with spelling correction.

***This module exports***

Classes:
Corrector -- Class to give spelling suggestions for strings.

Module-level functions:
matchScore -- Returns the matchScore of two sequences.
"""

# Public interface
__all__ = ["Corrector", "matchScore"]

# Imports
import spellingbeecc as sbcc


class Corrector:

    """Class to give spelling suggestions for strings.

    Methods:
    correct() -- give spelling suggestions for a string

    Instance variables:
    wordlist -- A file object representing a list of words to consider 
        correct. YOU MUST CLOSE THIS FILE YOURSELF.
    threshold -- a number used to determine if a word is good enough to 
        be a spelling suggestion
    """

    def __init__(self, wordlist="words.txt", threshold=1):
        """Construct a new Corrector object.

        Arguments:
        wordlist -- either an already-opened file object or a filename 
            as string; the file is a newline separated list of words to 
            consider correctly spelled; this is assigned to 
            self.wordlist (optional, default "words.txt")
        threshold -- a number used to determine if a word is good 
            enough to be a spelling suggestion; the lesser, the stricter 
            the threshold; this is assigned to self.threshold (optional, 
            default 1)

        Other side effects:
            If wordlist is a filename, the file will be opened, but not 
            closed. YOU MUST CLOSE THE FILE YOURSELF.
        """

        if isinstance(wordlist, str):
            self.wordlist = open(wordlist)
        else:
            # wordlist argument is a file object
            self.wordlist = wordlist

        self.threshold = threshold

    def correct(self, string):
        """Give spelling suggestions for a string and return a list.

        Arguments:
        string -- string to correct

        Return value:
        Returns a list of dictionaries. The keys of the dictionaries are
        numbers or None. The values are lists. The keys are the values 
        returned by matchScore(), the string "nomatch", or None; the 
        lower the value, the better the match. 
        If a key is None, that is the only key; that word was spelled 
        correctly, and that key's value is a list containing only that 
        word.
        If a key is "nomatch", that is the only key; no suggestion below 
        self.threshold was found. That key's value is a list containing 
        only the original word.
        Otherwise, the lists contain strings -- words that had 
        that matchScore.
        """

        listOfWords = string.split()
        index = 0

        for x in listOfWords:
            candidates = {}

            for word in self.wordlist:
                x = x.lower()
                word = word[:-1].lower()

                if x == word:
                    candidates = {None: [word]}
                    # Some words may actually be spelled correctly!
                    break

                d = matchScore(x, word)
                if d < self.threshold:
                    if d in candidates:
                        candidates[d].append(word)
                    else:
                        candidates[d] = [word]

            if len(candidates) == 0:
                # If there were no candidates
                candidates = {"nomatch": [x]}

            listOfWords[index] = candidates
            index += 1
            self.wordlist.seek(0)

        return listOfWords


def matchScore(a, b):
    """Returns the matchScore of two sequences.

    Arguments:
    a, b -- Sequences.

    Return value:
    Returns (Levenshtein distance 
        - length of longest common subsequence) / 2.
    """

    return (sbcc.lev.lev(a, b) - sbcc.lcslen.lcsLen(a, b)) / 2

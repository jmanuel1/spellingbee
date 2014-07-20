"""autocorrect.py -- program to correct spelling of stdin.

Input is taken from sys.stdin, output goes to sys.stdout.

This program requires a file called "words.txt" in the current working 
directory; this file is a newline-separated list of words to consider 
correctly-spelled.

This script is kept here as an example of how to use the spellingbee 
module. It should not be used for production.
"""

import spellingbee


def joinIfNotEmpty(sep, base, *other):
    if base == "":
        return sep.join(other)
    else:
        return sep.join([base] + list(other))

correctStr = ""
corrector = spellingbee.Corrector()
suggestions = corrector.correct(input())

for suggest in suggestions:

    if None in suggest:
        # The word was spelled correctly.
        # str.join() RETURNS a string. str.join() is NOT in place.
        correctStr = joinIfNotEmpty(" ", correctStr, suggest[None][0])
    elif "nomatch" in suggest:
        # No suitable suggestion was found.
        correctStr = joinIfNotEmpty(" ", correctStr, suggest["nomatch"][0])
    else:
        # This word was corrected.
        key = sorted(suggest)[0]

        correctStr = joinIfNotEmpty(" ", correctStr, suggest[key][0])


print(correctStr)

# Remember to close files!
corrector.wordlist.close()

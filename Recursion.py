## Lab04- Recursion ##

# Print all words that are made of the characters in the array of letters.
# There may not be consecutive equal letters, so:
# aax is not allowed, but axa is allowed.
# @param length : the length of the words that are to be printed
# @param letters: the letters you should be using
# @precondition: letters contains at least 2 characters, and has no duplicates.

def printNoDoubleLetterWords(length, letters):
## do not change this method ##
    printNoDoubleLetterWords(length,"",letters)



# Print all words that are made of the characters in letters. There may not be consecutive equal letters,
#aax is not allowed, but axa is allowed.
#@param length : either how many more letters need to be
#@param word   : the partial word so far.
#@param letters: the letters you should be using

def printNoDoubleLetterWordsH(length, word, letters):
    ## YOU WRITE THIS METHOD ##
    print() # default placeholder



# Convert the integer to a String containing English words that are used to say the number.
# precondition: n > Integer.MIN_VALUE   && n <= Integer.MAX_VALUE
# it is noteworthy that Integer.MIN_VALUE will not be tested.
# toWords(0) returns "zero"
# toWords(340) returns "three hundred and forty"
# toWords(1000430) returns: "one million four hundred and thirty"
# toWords(-2101000442) returns: "negative two billion one hundred and one million four hundred and forty-two"

def toWords(n):
    ## THIS SHOULD BE A WRAPPER METHOD ##
    ## Write this method, and the recursive method it calls.

    return "" # default placeholder

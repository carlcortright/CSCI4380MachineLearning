################################################################################
# Carl Cortright
#
# caco7348
#
# carl.cortright@colorado.edu
#
# week 1
################################################################################

################################################################################
#
# Program for generating random strings of characters based on conditional
# probabilities of those characters applearing after eachother
# Date: 8/25/2016
# Author: Carl Cortright
#
################################################################################

import random

#
# Function that prints a string of 100 generated characters.
#
def printHundredCharacters():
    # Define the starting string where the first character is 'I'
    probString = "I"

    # Prep the random number generator
    random.seed()

    # Create a loop, that checks the last letter in the string, applies the
    # probabilities and appends the next letter to the string
    for num in range(0, 99):
        # Grab the last letter in the current string
        lastLetter = probString[len(probString) - 1]

        # Generate a random number to help calculate the next letter
        rand = random.random()

        # Apply the probabilities (ugly decission tree), cleanest way
        newLetter = ""
        if(lastLetter == "I"):
            # The probability of a _ is 1
            newLetter = "_"
        elif(lastLetter == "_"):
            if(rand < 0.5):
                newLetter = "a"
            elif(rand >= 0.5):
                newLetter = "l"
        elif(lastLetter == "a"):
            if(rand < 0.4):
                newLetter = "m"
            elif(rand >= 0.4):
                newLetter = "l"
        elif(lastLetter == "m"):
            if(rand < 0.8):
                newLetter = "_"
            elif(rand >= 0.8):
                newLetter = "!"
        elif(lastLetter == "l"):
            newLetter = "i"
        elif(lastLetter == "i"):
            if(rand < 0.95):
                newLetter = "v"
            elif(rand >= 0.95):
                newLetter = "n"
        elif(lastLetter == "v"):
            newLetter = "e"
        elif(lastLetter == "n"):
            newLetter = "e"
        elif(lastLetter == "e"):
            newLetter = "!"
        elif(lastLetter == "!"):
            if(rand < 0.7):
                newLetter = "_"
            elif(rand >= 0.7 and rand < 0.9):
                newLetter = "I"
            elif(rand >= 0.9):
                newLetter = "!"


        # Append the new letter to the end of the string
        probString += newLetter

    # Print the string to the console
    print(probString)


# Print 10 lines of the generated characters to the console
for num in range(0, 10):
    printHundredCharacters()

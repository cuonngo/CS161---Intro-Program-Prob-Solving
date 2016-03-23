# Copyright(c) 2011 Cuong Ngo
# Print the most character used in a sentence

list1 = []
spaces = " "

# Get the sentence
SENTENCE = input("sentence: ")
print(SENTENCE)

# Lowercase
sentence = SENTENCE.lower()

# Get rid of the space in a sentence
sentence = sentence.replace(" ", "")

# Convert sentence to integer number and put it in a list
for letter in sentence:
    number = ord(letter)    
    list1.append(number)

# Find the mode
mode = max([list1.count(y),y] for y in list1) [1]
print("2", chr(mode))

# Exit the program
input("\n\nPress the enter key to exit.")

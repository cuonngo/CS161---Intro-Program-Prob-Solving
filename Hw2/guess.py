# Copyright (c) 2011 Cuong Ngo
# Guessing game

print("\tThink of a number between 1 and 10, but don't tell me what it is.\n")
print("\tThen hit enter.\n\n\n")
number = 5
answer = ""
while answer != "y":
    answer = input("\nIs it " + str(number) + "? [y/n]")
    if answer == "n":
        answer = input("\nIs your number higher or lower than " + str(number) + "? [h/l]")
        if answer == "l":
            number -= 1
            if number < 0:
                break
        elif answer == "h":
            number += 1
            if number > 10:
                break
else:
    print("\nI win!")

input("\n\nPress enter key to exit.")

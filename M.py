import sys
import stdio
import stddraw
import numpy
import stdarray

# Randomly crack one hundred passwords and
#  display number of guesses for each, then average for all.

import random

# Target password to crack
target_password = ""

# Characters to create random passwords
characters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# Flag to stop guessing when attempt is sucessfull
attempts = "yes"

# The number of characters to create and guess
password_length = 4

# Store the number of guesses for each sucessfull password crack
guesses = 0
# Number of passwords to crack, [counter, quota]
reps = [0, 1000]

# Generate random password guesses and compare to target password until match found.
def crackedout():
    # global target_password, status, password_length, guesses
    # Current number of guesses
    count = 0
    while attempts == "yes":
        guess = ""
        # Create a string from randomly chosen characters
        while len(guess) < password_length:
            # Add a random index from the characters list
            guess += random.choice(characters)
        # Compare guess to the real password
        if guess == target_password:
            print("Password cracked!: " + str(guess))
            status = "finished"
            count += 1
            print(str(count) + " guesses")
            # Add number of guesses for this run
            guesses += count
        else:
            count += 1

# Generate random target passwords and crack each until quota is reached
while reps[0] < reps[1]:
    reps[0] += 1
    status = "ongoing"
    target_password = ""
    # Create a string from randomly chosen characters
    while len(target_password) < password_length:
        # Add a random index from the characters list
        target_password += random.choice(characters)
    # Run crack function against new password
    crackedout()


# Divide total guesses by number of passwords cracked to get average
avg = guesses / reps[1]
print(str(reps[1]) + " passwords cracked.")
print("Average: " + str(avg) + " guesses per password.")
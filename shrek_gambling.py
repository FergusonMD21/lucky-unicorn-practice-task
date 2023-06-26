# Imports the libraries useed in the program
import random
import time

# The list of tokens from which one will be randomly selected
# The lower value items are repeated to decrease the cance of getting the Shrek token
tokens = ["shrek", "puss in boots", "puss in boots", "donkey", "donkey", "lord farquad", "lord farquad", "lord farquad", "lord farquad", "lord farquad", "lord farquad",]

# Explain Shrek Gambling to the user with a 1 second delay between each set of text
print("Welcome to Shrek Gambling!")
time.sleep(1)
print("To play, first you must enter your starting amount. This can be a number from $1 to $5, but the most you can spend on this game in total is $10.")
time.sleep(1)
print("You will then recieve token which is either a Shrek, Puss in Boots, Donkey, or Lord Farquad")
time.sleep(1)
print("A Shrek will earn 3 times your bet, a Donkey or a Puss in Boots will earn half your bet, and a Lord Farquad will earn nothing")
time.sleep(1)
input("Press enter your bet:  ")

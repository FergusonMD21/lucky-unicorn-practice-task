# Imports the libraries useed in the program
import random
import time

# The list of tokens from which one will be randomly selected
# The lower value items are repeated to decrease the cance of getting the Shrek token
tokens = {"Shrek": 4, "Puss in Boots" : 0.5, "Puss in Boots" : 0.5, "Donkey" : 0.5, "Donkey" : 0.5, "Lord Farquad" : 0, "Lord Farquad" : 0, "Lord Farquad" : 0, "Lord Farquad" : 0, "Lord Farquad" : 0, "Lord Farquad" : 0}

total_spent = 0
total_earnings = 0

# Explains Shrek Gambling to the user with a 1 second delay between each set of text
print("Welcome to Shrek Gambling!")
time.sleep(1)
print("To play, you must first enter your starting amount. This can be a number from $1 to $5, but the most you can spend on this game in total is $10.")
time.sleep(1)
print("You will then recieve token which is either a Shrek, Puss in Boots, Donkey, or Lord Farquad")
time.sleep(1)
print("A Shrek will earn 4 times your bet, a Donkey or a Puss in Boots will earn half your bet, and a Lord Farquad will earn nothing")

# Will repeat until the user quits or until the maximum spend has been reached
while True:
    time.sleep(1)
    try:
        # Ensures that the user cannot spend more than $10
        if total_spent >= 10:
            print("You have reached the maximum amount you can spend on this game. Goodbye!")
            break

        # Asks the user to enter their starting bet
        bet = input("Press enter your bet or type 'quit' to exit:  ")

        # If the user enters 'quit', the program will exit
        if bet == "quit":
            break

        # Sets the bet to an integer
        bet = int(bet)

        # If the chosen bet would cause the user to spend more than $10, The bet will not be allowed, and the while loop will restart
        if bet > 10 - total_spent:
            print(f"You cannot spend this amount, as it will take you over $10. The maximum you can spend is {10 - total_spent}")
            continue

        # Adds the bet to the total spent, so the program can know if the user has spent too much
        total_spent += bet
    except ValueError:
        print("Please enter a whole number between 1 and 5 or type 'quit' to exit")
        continue
    if bet < 1 or bet > 5:
        print("Please enter a whole number between 1 and 5 or type 'quit' to exit")
        continue
    print("You have bet $" + str(bet))
    time.sleep(1)
    token = random.choice(list(tokens.keys()))
    print(token)
    print("Your token is a " + str(token))
    prize = bet * tokens[token]
    if token == "Shrek":
        print(f"You have won ${prize}! Well done!")
        continue
    elif token == "Puss in Boots" or token == "Donkey":
        print(f"You have won ${prize}")
    print("You have not won anything, maybe next time!")
    

    

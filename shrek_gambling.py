# Imports the libraries useed in the program
import random
import time

# The dictionary of tokens and token values from which one will be randomly selected
# The lower value items are repeated to decrease the cance of getting the Shrek token
tokens = {"Shrek": 4, "Puss in Boots" : 0.5, "Puss in Boots" : 0.5, "Donkey" : 0.5, "Donkey" : 0.5, "Lord Farquad" : 0, "Lord Farquad" : 0, "Lord Farquad" : 0, "Lord Farquad" : 0, "Lord Farquad" : 0, "Lord Farquad" : 0}

total_spent = 0
total_earnings = 0
max_spend = 5

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
    # Waits one second
    time.sleep(1)

    # This means if there is an error, the program will not stop, and instead go to the except condition
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

    # This means if there is a value error, like if the user puts letters in the input, an error message will be sent, and the loop will restart
    except ValueError:
        print(f"Please enter a whole number between 1 and {max_spend} or type 'quit' to exit")
        continue

    # If the bet is out of the range, an error message will be sent, and the loop will restart
    if bet < 1 or bet > 5:
        print(f"Please enter a whole number between 1 and {max_spend} or type 'quit' to exit")
        continue

    # If the chosen bet would cause the user to spend more than $10, The bet will not be allowed, and the while loop will restart
    if bet > max_spend:
        print(f"You cannot spend this amount, as it will take you over $10. The maximum you can spend is {max_spend}")
        continue

    # Adds the bet to the total spent, so the program can know if the user has spent too much
    total_spent += bet

    # Tells the user how much was bet
    print("You have bet $" + str(bet))

    # Wait one second
    time.sleep(1)

    # Selects a random token from the dictionary of tokens and token values
    token = random.choice(list(tokens.keys()))

    # Prints the token to the user
    print("Your token is a " + str(token))

    # Sets the value of the prize, based off of what token was chosen
    prize = bet * tokens[token]
    if token == "Shrek":
        print(f"You have won ${prize}! Well done!")
        continue
    elif token == "Puss in Boots" or token == "Donkey":
        print(f"You have won ${prize}")
    print("You have not won anything, maybe next time!")
    

    

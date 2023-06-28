# Imports the libraries used in the program
# The random library is used to pick a random token from the list
# The time library is used to wait time so not everything happens at once
import random
import time

# The dictionary of tokens and token values from which one will be randomly selected
# The lower value items are repeated to decrease the cance of getting the Shrek token
tokens = ["Shrek", "Puss in Boots", "Puss in Boots", "Puss in Boots", "Donkey", "Donkey", "Donkey", "Lord Farquad", "Lord Farquad", "Lord Farquad", "Lord Farquad", "Lord Farquad", "Lord Farquad", "Lord Farquad", "Lord Farquad", "Lord Farquad"]

total_spent = 0
total_earnings = 0
max_spend = 5

# Functions
def get_bet():
    # Imports global variables
    global total_spent, restart_loop, max_spend, total_earnings

    # This means if there is an error, the program will not stop, and instead go to the except condition
    try:
        # Ensures that the user cannot spend more than $10
        if total_spent >= 10:
            print("You have reached the maximum amount you can spend on this game.")

            time.sleep(1)

            # When the game loop is exited, the total earnings and spent amount will be printed to the user
            print(f"Thanks for playing! You earned ${'{:.2f}'.format(total_earnings)} and spent ${'{:.2f}'.format(total_spent)}")

            # Exit the program
            quit()

        # Sets the maximum spend amount to $5 if the total spent is less than or equal to $5, or to 10 - total spent if the total spent is greater than $5
        max_spend = 10 - total_spent if total_spent > 5 else 5

        # Tells the user how much they have spent and earned so far
        print(f"Currently, you have spent ${'{:.2f}'.format(total_spent)} and made ${'{:.2f}'.format(total_earnings)}")

        # Asks the user to enter their starting bet
        bet = input("Press enter your bet or type 'quit' to exit:  ")

        # If the user enters 'quit', the program will exit
        if bet == "quit":         
            profit_loss = "profit" if total_earnings > total_spent else "loss"

            # When the game loop is exited, the total earnings and spent amount will be printed to the user
            print(f"Thanks for playing! You earned ${'{:.2f}'.format(total_earnings)} and spent ${'{:.2f}'.format(total_spent)}, giving you a {profit_loss} of ${}")

            time.sleep(1)

            # Quits the program
            quit()

        # Sets the bet to an integer
        bet = round(float(bet), 2)

    # This means if there is a value error, like if the user puts letters in the input, an error message will be sent, and the loop will restart
    except ValueError:
        print("Bet amount must be a whole number between 1 and 5 or type 'quit' to exit")
        restart_loop = True
        return restart_loop

    # If the bet is out of the range, an error message will be sent, and the loop will restart
    if bet < 1 or bet > 5:
        print("Bet amount must be a whole number between 1 and 5 or type 'quit' to exit")
        restart_loop = True
        return restart_loop

    # If the chosen bet would cause the user to spend more than $10, The bet will not be allowed, and the while loop will restart
    if bet > max_spend:
        print(f"You cannot spend this amount, as it will take you over $10. The maximum you can spend is {max_spend}")
        restart_loop = True
        return restart_loop

    # Adds the bet to the total spent, so the program can know if the user has spent too much
    total_spent += bet

    # Tells the user how much was bet
    print("You have bet $" + str(bet))

    return bet

def shrek(bet):
    # Imports total_earnings from global scope
    global total_earnings

    # Sets the value of the prize, based off of what token was chosen
    prize = bet * 4

    # Adds the prize amount to the total earnings
    total_earnings += prize

    # Prints the prize amount to the user
    print(f"You have won ${prize}! Well done!")

def puss_or_donkey(bet):
    # Imports total_earnings from global scope
    global total_earnings

    # Sets the value of the prize, based off of what token was chosen
    prize = round((bet * 0.5), 2)

    # Adds the prize amount to the total earnings
    total_earnings += prize

    # Prints the prize amount to the user either in dollars, if the prize is greater than $1, or in cents if the prize is less than $1
    if prize >= 1:
        print(f"You have won ${prize}")
    else:
        print(f"You have won {prize * 100}c")

def farquad(bet):
    # Tells the user that nothing was won
    print(f"Sorry, you lost your bet of ${bet}. Maybe you'll win next time")


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
    restart_loop = False

    # Waits one second
    time.sleep(1)

    if (bet := get_bet()) == True:
        continue

    # Wait one second
    time.sleep(1)

    # Selects a random token from the dictionary of tokens and token values
    token = random.choice(tokens)

    # Prints the token to the user
    print("Your token is a " + str(token))

    # Shows the message and the prize amount to the user, depending on what token was selected
    if token == "Shrek":
        shrek(bet)
    elif token == "Puss in Boots" or token == "Donkey":
        puss_or_donkey(bet)
    else:
        farquad(bet)
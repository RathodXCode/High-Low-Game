#importing
import random
import easygui_qt as eg

#functions
def get_bet(credits):
    msg = "You have {} credits. How many credits do you want to bet?".format(credits)
    title = "High-Low Game"
    bet = None
    while bet is None:
        bet_str = eg.get_string(msg, title)
        if bet_str is None:
            return None
        try:
            bet = int(bet_str)
            if not 1 <= bet <= credits:
                eg.show_message("Please enter a bet between 1 and {}.".format(credits))
                bet = None
        except ValueError:
            eg.show_message("Please enter a valid integer.")
            bet = None
    return bet

#function to get player choice
def get_player_choice():
    choices = ["High", "Low"]
    reply = eg.get_choice("Choose High or Low", choices=choices)
    return reply

#function to determine result
def determine_result():
    number = random.randint(1, 13)
    if number >= 8:
        result = "High"
    elif number <= 6:
        result = "Low"
    else:
        result = "Tie"
    return number, result

#function to update credits
def update_credits(credits, bet, result, reply, number):
    if result == reply:
        credits += bet
        eg.show_message("The number was {}. Hoorey you won! You now have {} credits.".format(number, credits)) 
        choice = eg.get_choice("Do you want to play again?", choices=["YES", "NO", "EXIT"])
        return credits, choice
    elif result == "Tie":
        eg.show_message("The number was {}. It's a tie! You still have {} credits.".format(number, credits))
        choice = eg.get_choice("Do you want to play again?", choices=["YES", "NO", "EXIT"])
        return credits, choice
    else:
        credits -= bet
        eg.show_message("The number was {}. You lose! You now have {} credits. haha you lose better luck next time".format(number, credits))
        choice = eg.get_choice("Do you want to play again?", choices=["YES", "NO", "EXIT"])
        return credits, choice

#main function
def main():
    credits = 1000
    while credits > 0:
        bet = get_bet(credits)
        if bet is None:
            break

        reply = get_player_choice()
        if reply is None:
            break

        number, result = determine_result()
        credits, choice = update_credits(credits, bet, result, reply, number) #update credits

        if choice == "NO" or choice == "EXIT":
            break

    if credits <= 0:
        eg.show_message("You ran out of credits. Game over!")
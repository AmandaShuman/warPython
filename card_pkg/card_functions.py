from hashlib import new
import random
import time
import sys

#====================================================================================================
#                                     GLOBAL VARIABLES
#====================================================================================================
num_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

spade = chr(9824)
club = chr(9827)
heart = chr(9829)
diamond = chr(9830)
suits = [heart, spade, diamond, club]
deck = []


# ===================================================================================================
#                       FUNCTIONS TO BE USED FOR SEVERAL CARD GAMES
# ===================================================================================================
def full_deck():
    """
    Mixing two lists into one list by adding each element to the other
    Returns:
        A full shuffled deck where each numbered card gets a suit - repeated for each suit.
    """
    global deck
    for i in range(len(num_cards)):
        for j in range(len(suits)):
            card = num_cards[i] + suits[j]
            deck.append(card)
            random.shuffle(deck)
    return (deck)


def keep_playing():
    """
    Gives player option to continue playing or quit playing by typing "q" at any point.
    Returns:
        Allows player to continue with game OR to quit game.
    Raises:
        else: returns an exemption
    """
    while True:
        choice = input("Press Enter to keep playing or type 'Q' to quit:  ")
        if choice == "":
            choice = True
            break
        elif choice.capitalize() == "Quit" or choice.lower() == "q":
            print("OK, goodbye!")
            sys.exit()
        else:
            print('You have entered an invalid option. Please hit Enter or type "q"')
            continue


def starting_hand(deck, num_cards):
    """
    Make subdeck from given deck and removes subdeck cards from deck
    Arguments:
        deck - this is the beginning deck to pull cards from
        num_cards - the size of the subdeck you want
    Returns:
        player_hand - list containing the cards for the player
        deck - deck without player_hand cards in it (to be used for multiple players and/or computer for subsequent uses)
    """
    player_hand = []
    max_index = len(deck) - 1
    for _ in range(num_cards):
        # use _ instead of i when you don't need to use the variable
        card_pick = random.randint(0, max_index)
        player_hand.append(deck[card_pick])
        deck.pop(card_pick)
        max_index -= 1
    return player_hand, deck


#===================================================================================================
#                       FUNCTIONS FOR GO FISH
#===================================================================================================
def check_for_matches(player, deck, player_score):
    """
    Checks to see if there is a matching pair in the player's deck by sorting the deck and then looking at the first value of each string to compare equality.
    Args:
        player - the player/computer checking for matches
        deck - the player/computer's hand
        player_score - the current running score for the player
    Returns:
        deck - the player's hand after matches have been checked
        player_score - player's score after adding matches to it
    """
    deck.sort()
    deck_to_check = [card[0] for card in deck]
    points = player_score
    for card in deck_to_check:
        if deck_to_check.count(card) > 1:
            print(f"{player} got a match!")
            deck_to_check.remove(card)
            deck_to_check.remove(card)
            points += 2
    new_deck = [card for card in deck if card[0] in deck_to_check]
    return new_deck, points


def values_only(deck):  #fix this to account for 10 display
    """
    We only care about the value of the card in the deck, not the suit so we are taking out the values to compare.
    Arguments:
        deck - the deck you want to look at values
    Returns:
        Returns a list with only the first element of each string from the original deck
    """
    return [card[0] for card in deck]


def go_fish_ask(player_values, player_name):
    """
    Allows for a player to ask from a card from their deck
    Args:
        player_name - player's name for personalization
        player_values - the face value of the card w/o suit
    Returns:
        player_choice - the face value of the card the player chose
    """
    while True:
        print(f"Here are the cards you can ask for: {player_values}")
        player_choice = input("Which option do you want to ask the computer?  ")
        player_choice = player_choice.capitalize()
        if player_choice in player_values:
            print(f'{player_name} is asking, "Do you have any {player_choice}s?')
            time.sleep(2)
            break
        else:
            print(f"You have to pick a card from your list!")
    return player_choice


def go_fish_check(player_choice, player_points, player_deck, opponent_name, opponent_deck, remaining_deck):
    player_values = values_only(player_deck)
    opponent_values = values_only(opponent_deck)
    points = player_points
    if player_choice in opponent_values:
        print(f"{opponent_name} has a {player_choice}!")
        points += 2
        player_values.remove(player_choice)
        opponent_values.remove(player_choice)
        new_player_hand = [card for card in player_deck if card[0] in player_values]
        new_opponent_hand = [card for card in opponent_deck if card[0] in opponent_values]
        new_remaining_deck = remaining_deck[:]
    else:
        print(f"{opponent_name} doesn't have any {player_choice}'s. Go Fish!")
        new_opponent_hand = opponent_deck[:]
        card_pick = random.randint(0, (len(remaining_deck)-1))
        new_player_hand = player_deck.append(deck[card_pick])
        new_remaining_deck = remaining_deck[:]
        new_remaining_deck.pop(card_pick)
        points += 0

    return new_player_hand, new_opponent_hand, new_remaining_deck, points



# ====================================================================================================
#                       FUNCTIONS JUST FOR WAR (BUT USEFUL FOR COUNTING CARD VALUES)
# ====================================================================================================


def card_points(card):
    """
    Evaluates card points based on value of card incrementing up from 10, Jack, Queen, King, to Ace.
    Args:
        card - this is the card to check the value for
    Returns:
        points - the point value for the card 
    """
    if card[0] == "2":
        points = 2
    elif card[0] == "3":
        points = 3
    elif card[0] == "4":
        points = 4
    elif card[0] == "5":
        points = 5
    elif card[0] == "6":
        points = 6
    elif card[0] == "7":
        points = 7
    elif card[0] == "8":
        points = 8
    elif card[0] == "9":
        points = 9
    elif card[0] == "1":
        points = 10
    elif card[0] == "J":
        points = 11
    elif card[0] == "Q":
        points = 12
    elif card[0] == "K":
        points = 13
    else:
        points = 14
    return points


# ====================================================================================================
#                       FUNCTIONS NOT YET USED, BUT USEFUL FOR FUTURE
# ====================================================================================================
def subdeck(name):
    """
    Diving up a list into sublists based on user request. 
    Arguments:
        name: Name of subdeck requested (i.e. 4's or "Hearts")
    Returns:
        Returns a sublist containing only requested cards.
    """
    full_deck()
    sub_list = [card for card in deck if name in card]
    print(sub_list)


# ====================================================================================================
#                       DEV TESTING FUNCTIONS
# ====================================================================================================
def check_for_matches_check():
    trial_deck = ['5♥', '6♥', '7♠', '7♦', 'J♦', 'K♥', 'K♦']
    trial_score = 0
    trial_deck, trial_score = check_for_matches("You", trial_deck, trial_score)
    print(trial_deck)
    print(trial_score)

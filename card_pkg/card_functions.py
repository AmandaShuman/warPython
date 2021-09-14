# from hashlib import new
# from os import dup
import random
import time
import sys

# =============================================================================
#                                     GLOBAL VARIABLES
# =============================================================================
num_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

spade = chr(9824)
club = chr(9827)
heart = chr(9829)
diamond = chr(9830)
suits = [heart, spade, diamond, club]
deck = []


# =============================================================================
#                       FUNCTIONS TO BE USED FOR SEVERAL CARD GAMES
# =============================================================================
def full_deck():
    """
    Mixing two lists into one list by adding each element to the other
    Args:
        none
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
    Args:
        none
    Returns:
        Allows player to continue with game OR to quit game.
    Raises:
        else: returns an exemption if anything other than q or quit typed in
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
    Args:
        deck - this is the beginning deck to pull cards from
        num_cards - the size of the subdeck you want
    Returns:
        player_hand - list containing the cards for the player
        new_deck - deck without player_hand cards in it (to be used for multiple players and/or computer for subsequent uses)
    """
    player_hand = []
    new_deck = deck[:]
    max_index = len(deck) - 1
    for _ in range(num_cards):
        # use _ instead of i when you don't need to use the variable
        card_pick = random.randint(0, max_index)
        player_hand.append(deck[card_pick])
        new_deck.pop(card_pick)
        max_index -= 1
    return player_hand, new_deck


def who_wins(player_score, computer_score, player_hand, computer_hand):
    """
    Returns a message to the user about who won the game
    Args:
        player_score = the player's final score
        computer_score = the computer's final score
        player_hand = the cards in the player's hand
        computer_hand = the cards in the computer's hand
    """
    print("""
    ++++++++++++++++++++++++++++++++++++
            The game is over!
    ++++++++++++++++++++++++++++++++++++
    """)
    points_display(player_score, computer_score,
                   player_hand, computer_hand)
    if player_score > computer_score:
        print("You've won! Congrats!!")
    elif computer_score > player_score:
        print("Unfortunately, you've lost. Try again.")
    else:
        print("It's a tie!")
    sys.exit()


# =============================================================================
#                       FUNCTIONS FOR GO FISH
# =============================================================================
def check_for_matches(player, player_hand, player_score, player_values):
    """
    Checks to see if there is a matching pair in the player's deck by sorting the deck and then looking at the first value of each string to compare equality.
    Args:
        player - the player/computer checking for matches
        deck - the player/computer's hand
        player_score - the current running score for the player
        player_values - the value (without suit) 
    Returns:
        new_player_hand - the player's hand after matches have been checked
        points - player's score after adding matches to it
        new_player_values - the values in the player's hand (without suits)
    """
    player_hand.sort()
    points = player_score
    new_player_values = player_values[:]
    for card in new_player_values:
        if new_player_values.count(card) > 1:
            print(f"{player} got a pair of {card}s!")
            new_player_values.remove(card)
            new_player_values.remove(card)
            points += 2

    # convert player_hand list to a single string
    player_hand_string = ""
    for card in player_hand:
        player_hand_string += card + " "
    
    length = len(new_player_values)
    new_player_hand = []
    for i in range(length):
        value = new_player_values[i]
        index = player_hand_string.find(value)
        index_end = player_hand_string.find(" ", index)
        sliced_card = slice(index, index_end)
        card = player_hand_string[sliced_card]
        new_player_hand.append(card)

    return new_player_hand, points, new_player_values


def remove_paired_card(player_choice, player_hand):
    """
    Removes a card from a player's hand if a matching card is drawn.
    Args:
        player_choice = the value the player matched 
        player_hand = the cards in the player's hand
    Returns:
        new_hand = the new player's cards after the match has been removed
    """
    list = []
    list.append(player_choice)
    list = tuple(list)
    new_hand = [card for card in player_hand if not card.startswith(list)]
    return new_hand
    

def values_only(deck):  
    """
    We only care about the value of the card in the deck, not the suit so we are taking out the values to compare.
    Arguments:
        deck - the deck you want to look at values
    Returns:
        Returns a list with only the first element of each string from the original deck except for 2 first elements for 10.
    """
    return [card[:2] if card[0] == '1' else card[0] for card in deck]


def points_display(player_score, computer_score, player_hand, computer_hand):
    print(f"""---------------------------------------------
Scores:         You: {player_score}      || Computer: {computer_score}
---------------------------------------------
Card Count:     You: {len(player_hand)}      || Computer: {len(computer_hand)}
---------------------------------------------
    """)


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
        player_choice = input(
            "Which card do you want to ask for?  ")
        player_choice = player_choice.capitalize()
        if player_choice in player_values:
            print(f'{player_name} is asking, "Do you have any {player_choice}s?')
            time.sleep(2)
            break
        else:
            print(f"You have to pick a card from your list!")
    return player_choice


# =============================================================================
#         FUNCTIONS JUST FOR WAR (BUT USEFUL FOR COUNTING CARD VALUES)
# =============================================================================
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


# =============================================================================
#                       FUNCTIONS NOT YET USED, BUT USEFUL FOR FUTURE
# =============================================================================
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


# =============================================================================
#                       DEV TESTING FUNCTIONS
# =============================================================================
def testing_for_matches_check():
    trial_deck = ['10♥', '5♥', '6♥', '7♠', '7♦', 'J♦', 'K♥', 'K♦', 'K♦']
    player_values = ['10', '5', '6', '7', '7', 'J', 'K', 'K', 'K']
    trial_score = 0
    print("Here is the original hand:", trial_deck)
    trial_deck, trial_score, player_values = check_for_matches(
        "You", trial_deck, trial_score, player_values)
    print("Your hand", trial_deck)
    print("Your score:", trial_score)
    print("Player values:", player_values)


def testing_values_only():
    trial_deck = ['5♥', '6♥', '7♠', '10♥', 'J♦', 'K♥']
    player_values = values_only(trial_deck)
    print("Values you can play:", player_values)


if __name__ == '__main__':
    testing_for_matches_check()
    # testing_values_only()

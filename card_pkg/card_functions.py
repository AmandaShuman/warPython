import random
import sys

num_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

spade = chr(9824)
club = chr(9827)
heart = chr(9829)
diamond = chr(9830)
suits = [heart, spade, diamond, club]
deck = []


def full_deck():
    """
    Mixing two lists into one list by adding each element to the other
    Returns:
        A full deck where each numbered card gets a suit - repeated for each suit.
    """
    global deck
    for i in range(len(num_cards)):
        for j in range(len(suits)):
            card = num_cards[i] + suits[j]
            deck.append(card)
            random.shuffle(deck)
    return (deck)


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
    for i in range(num_cards):
        card_pick = random.randint(0, max_index)
        player_hand.append(deck[card_pick])
        deck.pop(card_pick)
        max_index -= 1
    return player_hand, deck


# def values_only(deck):
#     """
#     We only care about the value of the card in the deck, not the suit so we are taking out the values to compare.
#     Arguments:
#         deck - the deck you want to look at values
#     Returns:
#         Returns a list with only the first element of each string from the original deck
#     """
#     return [card[0] for card in deck]


def card_points(card):
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

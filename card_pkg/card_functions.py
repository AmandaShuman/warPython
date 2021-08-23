import random

num_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

spade = chr(9824)
club = chr(9827)
heart = chr(9829)
diamond = chr(9830)
suits = [heart, spade, diamond, club] 
deck = []

def full_deck():
    global deck
    for i in range(13):
        for j in range(4):
            card = num_cards[i] + suits[j]
            deck.append(card)
            random.shuffle(deck)
    return (deck)

def subdeck(name):
    full_deck()
    sub_list = [card for card in deck if name in card]
    print(sub_list)

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
    elif card[0] == "10":
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

import random

num_cards = ["2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King", "Ace"]
suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
deck = []

def full_deck():
    global deck
    for i in range(13):
        for j in range(4):
            card = num_cards[i] + " of " + suits[j]
            deck.append(card)
            random.shuffle(deck)
    return deck

def sublist(suit):
    global deck
    deck = full_deck()
    hearts = []
    spades = []
    diamonds = []
    clubs = []
    for i in range(13):
        heart_card = num_cards[i]+" of "+suits[0]
        hearts.append(heart_card)
        spade_card = num_cards[i]+" of "+suits[1]
        spades.append(spade_card)
        diamond_card = num_cards[i]+" of "+suits[2]
        diamonds.append(diamond_card)
        club_card = num_cards[i]+" of "+suits[3]
        clubs.append(club_card)

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

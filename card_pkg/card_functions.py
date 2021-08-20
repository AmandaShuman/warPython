import random

num_cards = ["2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King", "Ace"]
suits = ["Hearts", "Spades", "Diamonds", "Clubs"]

def full_deck():
    deck = []
    for i in range(13):
        for j in range(4):
            card = num_cards[i] + " of " + suits[j]
            deck.append(card)
            random.shuffle(deck)
    return deck


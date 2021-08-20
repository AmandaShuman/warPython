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
    print(deck)
'''
def sublist(suit):
    full_deck()
    sub_list = [k for k in full_deck() if 'suit' in k]
    print(sub_list)
sublist("Hearts")
'''
full_deck()
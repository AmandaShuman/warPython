import random

num_cards = ["1", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King", "Ace"]
suits = ["Hearts", "Spades", "Diamonds", "Clubs"]

#build deck of cards
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

deck_of_cards = hearts + diamonds + spades + clubs

#shuffle deck and separate into 2 piles for each player
player1_deck = random.sample(deck_of_cards, 26)
player2_deck = set(deck_of_cards) - set(player1_deck)

print(player1_deck)
print(player2_deck)

#time to play!
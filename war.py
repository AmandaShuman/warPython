num_cards = ["1", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King", "Ace"]
suits = ["Hearts", "Spades", "Diamonds", "Clubs"]

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
print(deck_of_cards)

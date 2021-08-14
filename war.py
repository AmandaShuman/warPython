num_cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
suits = ["Hearts", "Spades", "Diamonds", "Clubs"]

hearts = []
for i in range (13):
    heart_card = num_cards[i]+" of "+suits[0]
    hearts.append(heart_card)
print(hearts)

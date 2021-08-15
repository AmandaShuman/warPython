import random

num_cards = ["2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King", "Ace"]
suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
points = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

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
#card count
player1_score = len(player1_deck)
player2_score = len(player2_deck)

#draw 1 card from each pile until 1 person wins
card_num = 0
while player1_score < 52 and player2_score < 52:
    played_cards = []
    #print players' scores


    #pull a card from each player
    player1 = player1_deck[card_num]
    player2 = player2_deck[card_num]
    print(f"Player 1 has played the {player1}.")
    print(f"player 2 has played the {player2}.")

    #check to see who wins the match
    
    #add cards into a new pile and append it to the end of the winner's deck

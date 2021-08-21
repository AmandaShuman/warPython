import random
from card_pkg import card_functions

#shuffle deck and separate into 2 piles for each player
player1_deck = random.sample(card_functions.full_deck(), 26)
player2_deck = list(set(card_functions.full_deck()) - set(player1_deck))

#time to play!
#card count
player1_score = len(player1_deck)
player2_score = len(player2_deck)

#draw 1 card from each pile until 1 person wins
card_num = 0
while player1_score < 52 and player2_score < 52:
    #print players' scores
    print("\nPlayer 1 score: " + str(player1_score) + "   Player 2 score: " + str(player2_score))

    #pull a card from each player
    player1 = player1_deck[card_num]
    player2 = player2_deck[card_num]
    print(f"Player 1 has played the {player1}.")
    print(f"player 2 has played the {player2}.")
    card_num += 1

    #add cards into a new pile and append it to the end of the winner's deck
    player1_deck.remove(player1)
    player2_deck.remove(player2)
    playing_pile = []
    playing_pile.append(player1)
    playing_pile.append(player2)

    #check to see who wins the match
    p1_points = card_functions.card_points(player1)
    p2_points = card_functions.card_points(player2)

    if p1_points > p2_points:
        print("Player 1 has won this round.")
        player1_deck.extend(playing_pile)
        playing_pile = []
    elif p1_points < p2_points:
        print("Player 2 has won this round.")
        player2_deck.extend(playing_pile)
        playing_pile = []
    else:
        print("There's a tie! Time for war!")
    break

# This is the code to play the card game War

import random
import sys
from card_pkg import card_functions

# shuffle deck and separate into 2 piles for each player
player1_deck = random.sample(card_functions.full_deck(), 26)
player2_deck = list(set(card_functions.full_deck()) - set(player1_deck))

# initialize card count variables
player1_score = 26
player2_score = 26

# withdraw 1 card from each pile until 1 person wins
while True:
    if player1_score == 52:
        print("You've won! congrats!")
        sys.exit()
    elif player2_score == 52:
        print("The computer has won. Feel free to play the game again!")
        sys.exit()
    else:
        # initial card count
        player1_score = len(player1_deck)
        player2_score = len(player2_deck)

        # print players' scores
        print("\nYour score: " + str(player1_score) +
              "   computer score: " + str(player2_score))

        # pull a card from each player
        player1 = player1_deck[0]
        player2 = player2_deck[0]
        print(f"Your card: {player1}    computer card: {player2}")

        # add cards into a new pile and append it to the end of the winner's deck
        player1_deck.remove(player1)
        player2_deck.remove(player2)
        playing_pile = []
        playing_pile.append(player1)
        playing_pile.append(player2)

        # check to see who wins the match
        p1_points = card_functions.card_points(player1)
        p2_points = card_functions.card_points(player2)

        while True:
            if p1_points > p2_points:
                print("You have won this battle.")
                player1_deck.extend(playing_pile)
                playing_pile = []
                break
            elif p1_points < p2_points:
                print("The computer has won this battle.")
                player2_deck.extend(playing_pile)
                playing_pile = []
                break
            else:
                while p1_points == p2_points:
                    print("There's a tie! Time for war!")
                    if len(player1_deck) < 3:
                        print(
                            "You doesn't have enough cards and have lost by default. Computer wins the game of war. Play again to try your luck!")
                        sys.exit()
                    elif len(player2_deck) < 3:
                        print(
                            "The computer doesn't have enough cards and has lost by default. You have won the game of war! Congrats!")
                        sys.exit()
                    else:
                        p1_war = player1_deck[0:3]
                        p2_war = player2_deck[0:3]
                        playing_pile.extend(p1_war)
                        playing_pile.extend(p2_war)
                        player1_deck = [
                            card for card in player1_deck if card not in playing_pile]
                        player2_deck = [
                            card for card in player2_deck if card not in playing_pile]
                        p1_points = card_functions.card_points(p1_war[-1])
                        p2_points = card_functions.card_points(p2_war[-1])
                        print(
                            f"War! Both players have laid down 2 facedown cards each. \nYour card: {p1_war[-1]}     computer card: {p2_war[-1]}.")
                        break

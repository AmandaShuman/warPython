# This is the code to play the card game go Fish
import time
from card_pkg.card_functions import full_deck, starting_hand

# print("             Go fish")
# print("\nTHE RULES")
# time.sleep(1)

# print("""Each player is dealt a hand of 7 cards.

# If either player has a pair, they pull the pair from their hands and place them on the table.
# """)
# time.sleep(3)

# print("""You get to go first. Pick a card in your hand that you are trying to match, and say, “Do you have a Jack?”

# If the computer has a Jack, the you get that card and place both Jacks on the table. Then you go again. """)
# time.sleep(3)

# print("""
# If the computer doesn’t have a Jack, they say “Go Fish!” and you draw a card from the deck and put it in your hand.""")
# time.sleep(2)

# print("""
# If the drawn card is the card you asked for, you place the pair on the table and go again.
# If the drawn card matches any other card in your hand, you place the pair on the table but don’t go again. 
# Then the computer will have its turn to do the same.""")
# time.sleep(2)

# print("""
# The game is over whenever one player runs out of cards.
# The player with the most pairs at the end of the game wins, regardless of who ran out of cards first. """)
# time.sleep(3)

# print("""
# -------------------------------------------------------
#                     Time to Play!!
# -------------------------------------------------------""")

player_hand, remaining_deck = starting_hand(full_deck(), 7)
computer_hand, remaining_deck = starting_hand(remaining_deck, 7)
print("Here is your hand:", player_hand)
player_hand.sort()
print("Here is your sorted hand", player_hand)


"""
def check_for_matches(deck, score):
    deck.sort()
    for i in len(deck) - 2:  # need -2 to account for i+1
        if deck[i][0] == deck[i+1][0]:
            print("Got a match!")
            deck.pop(i)
            deck.pop(i+1)
            score += 2
    return deck, score 
"""




"""
Report the number of cards in the player’s hand, and the computer’s hand. Report the number of turns that have been played. Keep track of the pairs that each player has won, and display the number of pairs won by each player.

If the computer player in your Go Fish game makes moves by randomly choosing a card in its hand to ask you about, you have a very weak Go Fish player. Consider a strategy for playing Go Fish well, and implement that strategy in code. For example, a good Go Fish player remembers when the other player has asked about a card. Your computer player should do this as well!
"""



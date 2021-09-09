# This is the code to play the card game go Fish
import time
from card_pkg import card_functions

print("             Go fish")
print("\nTHE RULES")
time.sleep(1)

print("""Each player is dealt a hand of 7 cards.

If either player has a pair, they pull the pair from their hands and place them on the table.
""")
time.sleep(3)

print("""You get to go first. Pick a card in your hand that you are trying to match, and say, “Do you have a Jack?”

If the computer has a Jack, the you get that card and place both Jacks on the table. Then you goe again. """)
time.sleep(3)

print("""
If the computer doesn’t have a Jack, they say “Go Fish!” and you draw a card from the deck and put it in your hand.""")
time.sleep(2)

print("""
If the drawn card is the card you asked for, you place the pair on the table and go again.
If the drawn card matches any other card in your hand, you place the pair on the table but don’t go again. 
Then the computer will have its turn to do the same.""")
time.sleep(2)

print("""
The game is over whenever one player runs out of cards.
The player with the most pairs at the end of the game wins, regardless of who ran out of cards first. """)
time.sleep(3)

print("""
-------------------------------------------------------
                    Time to Play!!
-------------------------------------------------------""")











# user_hand = random.sample(card_functions.full_deck(), 7)

"""
Report the number of cards in the player’s hand, and the computer’s hand. Report the number of turns that have been played. Keep track of the pairs that each player has won, and display the number of pairs won by each player.

If the computer player in your Go Fish game makes moves by randomly choosing a card in its hand to ask you about, you have a very weak Go Fish player. Consider a strategy for playing Go Fish well, and implement that strategy in code. For example, a good Go Fish player remembers when the other player has asked about a card. Your computer player should do this as well!
"""



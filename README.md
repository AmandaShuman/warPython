### Game of war in Python

The goal is to be the first player to win all 52 cards

## THE DEAL
The deck is divided evenly, with each player receiving 26 cards, dealt one at a time, face down. Anyone may deal first. Each player places their stack of cards face down, in front of them.

## THE PLAY
Each player turns up a card at the same time and the player with the higher card takes both cards and puts them, face down, on the bottom of his stack.

If the cards are the same rank, it is War. Each player turns up two cards face down and one card face up. The player with the higher cards takes both piles (eight cards). If the turned-up cards are again the same rank, each player places another 2 cards face down and turns another card face up. The player with the higher card takes all 14 cards, and so on. If a player does not have enough cards for war, that person loses war by default. For the purpose of clarity, ace is high for scoring purposes.

## HOW TO KEEP SCORE
The game ends when one player has won all the cards.

# Skills learned
1 - using nested for loops to combine 2 lists
2 - using set() to find the compliment of a list when order doesn't matter
3 - using extend() to add one list of elements into another list to have one list instead of 2
4 - understanding list comprehensions (https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
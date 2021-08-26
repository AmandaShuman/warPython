### card games in Python
This file contains card games that can be played with a computer. See below for details on different games currently available in the options.


## War
This is the first card game added. As more games are added, there will be options added to choose which game to play!

# Skills learned
1 - using nested for loops to combine 2 lists
2 - using set() to find the compliment of a list when order doesn't matter
3 - using extend() to add one list of elements into another list to have one list instead of 2
4 - understanding list comprehensions (https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
5- using unicode for cards 

# Go fish rules
Use your class-based deck of cards to implement a game of Go Fish that you can play against the computer. A basic Go Fish game has the following rules:

Each player is dealt a hand of 7 cards.
If either player has a pair, they pull the pair from their hands and place them on the table.
One player goes first. The player picks a card in their hand that they’re trying to match, and they say, “Do you have a Jack?”
If the other player has a Jack, the asking player gets that card and places both Jacks on the table. The asking player goes again.
If the other player doesn’t have a Jack, they say “Go Fish!” The asking player draws a card from the deck and puts it in their hand.
If the drawn card is the card they asked for, they place the pair on the table and go again.
If the drawn card matches any other card in their hand, they place the pair on the table but don’t go again.
The game is over whenever one player runs out of cards.
The player with the most pairs at the end of the game wins, regardless of who ran out of cards first.
Report the number of cards in the player’s hand, and the computer’s hand. Report the number of turns that have been played. Keep track of the pairs that each player has won, and display the number of pairs won by each player.

If the computer player in your Go Fish game makes moves by randomly choosing a card in its hand to ask you about, you have a very weak Go Fish player. Consider a strategy for playing Go Fish well, and implement that strategy in code. For example, a good Go Fish player remembers when the other player has asked about a card. Your computer player should do this as well!

Extension: Write a version of this game where the computer plays itself.
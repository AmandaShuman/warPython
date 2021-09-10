# This is where the rules of each game will be set up as a function to be called to its specific game.

import time

def war_rules():
    print("                       Welcome to the Game of war")


    time.sleep(1)

    print("The goal is to be the first player to win all 52 cards")
    time.sleep(2)

    print("""
    ## THE DEAL
    The deck is divided evenly, with each player receiving 26 cards, dealt one at a time, face down. Anyone may deal first. Each player places their stack of cards face down, in front of them.""")
    time.sleep(2)

    print("""
    ## THE PLAY
    Each player turns up a card at the same time and the player with the higher card takes both cards and puts them, face down, on the bottom of his stack.""")
    time.sleep(2)

    print("""
    If the cards are the same rank, it is War. Each player turns up two cards face down and one card face up. The player with the higher cards takes both piles (eight cards). If the turned-up cards are again the same rank, each player places another 2 cards face down and turns another card face up. The player with the higher card takes all 14 cards, and so on. If a player does not have enough cards for war, that person loses war by default. For the purpose of clarity, ace is high for scoring purposes.""")
    time.sleep(4)

    print("""
    ## HOW TO KEEP SCORE
    Your score is the number of cards in your deck.
    The game ends when one player has won all the cards.

    -------------------------------------------------------
                        Time to Play!!
    -------------------------------------------------------""")

    time.sleep(2)


def go_fish_rules():
    print("             Go fish")
    print("\nTHE RULES")
    time.sleep(1)

    print("""Each player is dealt a hand of 7 cards.

    If either player has a pair, they pull the pair from their hands and place them on the table.
    """)
    time.sleep(3)

    print("""You get to go first. Pick a card in your hand that you are trying to match, and say, “Do you have a Jack?”

    If the computer has a Jack, the you get that card and place both Jacks on the table. Then you go again. """)
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
